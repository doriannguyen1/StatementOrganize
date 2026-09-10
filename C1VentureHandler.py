import csv
from Categories import get_category

class C1VentureHandler:
    """Handler for Capital One Venture card statements."""
    
    @staticmethod
    def process(reader, writer, filename):
        """Process C1 Venture CSV data."""
        for row in reader:
            try:
                date = row[0]
                # Amount is in row[5] (Debit) or row[6] (Credit)
                amount = row[5] if row[5] else row[6]
                description = row[3]
                
                # Get category
                category = get_category(description)
                
                new_row = [date, amount, description, category, "C1 VentureX"]
                writer.writerow(new_row)
            except IndexError:
                pass
