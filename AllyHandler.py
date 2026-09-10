import csv
from Categories import get_category
from Utils import contains

class AllyHandler:
    """Handler for Ally Bank statements with categorized transactions."""
    
    INCOME_SOURCES = ["VENMO CASHOUT", "CAPITAL ONE SERV REG.SALARY", "MSPBNA ACH TRNSFR", "PAYPAL TRANSFER", "Interest Paid", "CAPITAL ONE SERV PAYROLL", "ATM Fee Reimbursement", "JP Morgan Chase PAYMENT~", "FIDELITY INVESTM CLAIM REIM"]
    
    EXPENSES_SOURCES = ["VENMO PAYMENT", "BILT CARD HOUSING", "VENMO *", "DOMINION ENERGY BILLPAY"]
    
    TRANSFER_IN_SOURCES = ["Overdraft Transfer from Savings Account", "Internet transfer from Savings account"]
    
    TRANSFER_OUT_SOURCES = ["SCHWAB BROKERAGE MONEYLINK", "CHASE CREDIT CRD AUTOPAY", "WF Credit Card AUTO PAY", "CAPITAL ONE CRCARDPMT", "AMEX EPAYMENT ACH PMT", "Internet transfer to Savings account", "ADVS ED SERV PPD STUDNTLOAN", "CITI AUTOPAY PAYMENT", "Internet transfer from Savings account XXXXXX9263", "SCHWAB BROKERAGE MONEYLINK", "BILT CARD PMT", "CHASE CREDIT CRD EPAY"]
    
    @staticmethod
    def process(reader, writer, filename):
        """Process Ally Bank CSV data with transaction categorization."""
        income = []
        expenses = []
        transfer_in = []
        transfer_out = []
        other = []
        
        # Categorize transactions
        for row in reader:
            if contains(row[3], "Deposit"):
                if any(contains(row[4], sub) for sub in AllyHandler.INCOME_SOURCES):
                    income.append(row)
                elif any(contains(row[4], sub) for sub in AllyHandler.TRANSFER_IN_SOURCES):
                    transfer_in.append(row)
                else:
                    other.append(row)
            if contains(row[3], "Withdrawal"):
                if any(contains(row[4], sub) for sub in AllyHandler.TRANSFER_OUT_SOURCES):
                    transfer_out.append(row)
                elif any(contains(row[4], sub) for sub in AllyHandler.EXPENSES_SOURCES):
                    expenses.append(row)
                else:
                    other.append(row)
        
        # Write categorized sections
        sections = [
            ("INCOME", income),
            ("EXPENSES", expenses),
            ("TRANSFER IN", transfer_in),
            ("TRANSFER OUT", transfer_out),
            ("OTHER", other)
        ]
        
        for section_label, trans_type in sections:
            writer.writerow([section_label])  # Section header
            for row in trans_type:
                try:
                    AllyHandler.write_section(writer, section_label, row)
                except IndexError:
                    pass
            writer.writerow([])  # Empty line between sections
    
    @staticmethod
    def write_section(writer, section_label, row):
        """Write transaction based on section type."""
        date = row[0]
        amount = row[2]
        description = row[4]
        
        if section_label == "INCOME":
            category = AllyHandler.get_income_category(description)
            new_row = [date, amount, description, "Ally Checking", category]
            writer.writerow(new_row)
            
        elif section_label == "TRANSFER IN":
            new_row = [date, amount, description, "", "Ally Checking"]
            writer.writerow(new_row)
            
        elif section_label == "TRANSFER OUT":
            # Make amount positive
            try:
                amount = str(abs(float(amount)))
            except:
                pass
            new_row = [date, amount, description, "Ally Checking", ""]
            writer.writerow(new_row)
            
        elif section_label == "EXPENSES":
            category = AllyHandler.get_expense_category(description)
            # Make amount positive
            try:
                amount = str(abs(float(amount)))
            except:
                pass
            new_row = [date, amount, description, category, "Ally Checking"]
            writer.writerow(new_row)
            
        else:  # OTHER section
            del row[1]
            del row[2]
            if '-' in row[1]:
                try:
                    row[1] = str(float(row[1]) * -1)
                except:
                    pass
            writer.writerow(row)
    
    @staticmethod
    def get_income_category(description):
        """Get category for income transaction."""
        if any(keyword in description for keyword in ["CAPITAL ONE", "MSPBNA", "FIDELITY INVESTM"]):
            return "Capital One"
        elif "PAYPAL" in description:
            return "PayPal"
        elif "VENMO" in description:
            return "Venmo"
        elif "Zelle" in description:
            return "Zelle"
        else:
            return "Misc"
    
    @staticmethod
    def get_expense_category(description):
        """Get category for expense transaction."""
        if "AUTOMATIC PAYMENT" in description and "THANK YOU" in description:
            return "Ally Checking"
        elif "DOMINION ENERGY" in description or "BILLPAY" in description:
            return "Housing"
        elif "BILT CARD HOUSING" in description:
            return "Housing"
        elif "Zelle payment" in description:
            return "Housing"
        elif "FAMILYMART" in description or "SEVEN BANK" in description:
            return "JPN2026"
        elif "VENMO *TANYA MEKA" in description:
            return "Pookie Purchase"
        elif "APPLE CASH SENT MONEY" in description:
            return "Fun"
        elif "IRS USATAXPYMT" in description:
            return "Misc."
        else:
            return ""
