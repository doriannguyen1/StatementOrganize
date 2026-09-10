import csv
from Categories import get_category

class ChaseHandler:
    """Handler for Chase credit card statements."""
    
    @staticmethod
    def process(reader, writer, filename):
        """Process Chase CSV data."""
        for row in reader:
            try:
                date = row[0]
                description = row[2]
                amount = row[5]
                
                # Convert negative amounts to positive
                try:
                    amt_float = float(amount)
                    if amt_float < 0:
                        amount = str(abs(amt_float))
                except:
                    pass
                
                # Get category
                category = get_category(description)
                
                # Determine card type from filename
                card_type = ChaseHandler.get_card_type(filename)
                
                new_row = [date, amount, description, category, card_type]
                writer.writerow(new_row)
            except IndexError:
                pass
    
    @staticmethod
    def get_card_type(filename):
        """Determine Chase card type from filename."""
        if "0611" in filename:
            return "Chase Sapphire Reserve"
        elif "3673" in filename:
            return "Chase Freedom Unlimited"
        elif "8495" in filename:
            return "Chase Sapphire Preferred"
        elif "9243" in filename:
            return "Chase Freedom Flex"
        elif "0809" in filename:
            return "Chase United Explorer"
        else:
            return "Chase"
