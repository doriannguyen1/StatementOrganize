import csv

from utils.Categories import get_category

class AmexHandler:
    """Handler for Amex credit card statements."""
    
    @staticmethod
    def process(reader, writer, filename):
        """Process Amex CSV data."""
        for row in reader:
            try:
                date = row[0]
                description = row[1]
                amount = row[2]
                
                # Get category
                category = get_category(description)
                
                new_row = [date, amount, description, category, "Amex Gold"]
                writer.writerow(new_row)
            except IndexError:
                pass
