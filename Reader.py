import csv
import os
from Helper import cleanBilt, cleanC1, cleanChase, cleanAmex

def contains(haystack, needle):
    """Case-insensitive substring check. Returns False for None/empty inputs."""
    if not haystack or not needle:
        return False
    return needle.strip().lower() in haystack.strip().lower()

class Reader:
    def __init__(self):
        self = self

    def read(self, filename):
        # keep original filename for reading/writing, use a lowercased
        # copy for case-insensitive matching
        lname = filename.lower()
        intput_filename = 'input/' + filename
        print(intput_filename)
        output_filename = 'output/' + filename
        os.makedirs('output', exist_ok=True)
        with open(intput_filename, newline='') as csvfile, open(output_filename, 'w', newline='') as outfile:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(outfile, delimiter=',')
            if "c1" in lname or "transaction_download" in lname:
                for row in reader:
                    try:
                        row = cleanC1(row)
                        writer.writerow(row)
                    except IndexError:
                        pass

                    
            elif "chase" in lname:
                for row in reader:     
                    try:
                        row = cleanChase(row)
                        writer.writerow(row)
                    except IndexError:
                        pass

            elif "bilt" in lname:
                for row in reader: 
                    try:
                        row = cleanBilt(row)
                        writer.writerow(row)
                    except IndexError:
                        pass
            elif "amex" in lname or "activity" in lname:
              for row in reader:     
                try:
                    print(row)
                    desc = row[1]
                    amt = row[2]
                    row[1] = amt
                    row[2] = desc
                    writer.writerow(row)
                except IndexError:
                    pass
            elif "ally" in lname or "transactions" in lname:
                income_sources = ["VENMO CASHOUT", "CAPITAL ONE SERV REG.SALARY", "MSPBNA ACH TRNSFR", "PAYPAL TRANSFER", "Interest Paid", "CAPITAL ONE SERV PAYROLL", "ATM Fee Reimbursement", "JP Morgan Chase PAYMENT~"]
                expenses_sources = ["VENMO PAYMENT","BILT CARD HOUSING","VENMO *","DOMINION ENERGY BILLPAY" ]
                transfer_in_sources = ["Overdraft Transfer from Savings Account","Internet transfer from Savings account"]
                transfer_out_sources = ["SCHWAB BROKERAGE MONEYLINK","CHASE CREDIT CRD AUTOPAY", "WF Credit Card AUTO PAY", "CAPITAL ONE CRCARDPMT", "AMEX EPAYMENT ACH PMT", "Internet transfer to Savings account", "ADVS ED SERV PPD STUDNTLOAN", "CITI AUTOPAY PAYMENT","Internet transfer from Savings account XXXXXX9263","SCHWAB BROKERAGE MONEYLINK", "BILT CARD PMT","CHASE CREDIT CRD EPAY"]
                income = []
                expenses = []
                transfer_in = []
                transfer_out = []
                other = []
                for row in reader:
                    if contains(row[3], "Deposit"):
                        if any(contains(row[4], sub) for sub in income_sources):
                            income.append(row)
                        elif any(contains(row[4], sub) for sub in transfer_in_sources):
                            transfer_in.append(row)
                        else:
                            other.append(row)
                    if contains(row[3], "Withdrawal"):
                        if any(contains(row[4], sub) for sub in transfer_out_sources):
                            transfer_out.append(row)
                        elif any(contains(row[4], sub) for sub in expenses_sources):
                            expenses.append(row)
                        else:
                            other.append(row)

                res = [income, expenses, transfer_in, transfer_out, other]
                for trans_type in res:
                    for row in trans_type:
                        try:
                            del row[1]
                            del row[2]
                            if '-' in row[1]:
                                try:
                                    row[1] = str(float(row[1]) * -1)
                                except:
                                    pass
                            writer.writerow(row)
                        except IndexError:
                            pass
                    writer.writerow([])
                
                    
  