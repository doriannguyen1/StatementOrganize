import csv
from Helper import cleanC1, cleanBilt

class C1Handler:
    """Handler for Capital One (non-Venture) card statements."""
    
    @staticmethod
    def process(reader, writer, filename):
        """Process C1 CSV data using legacy cleaning function."""
        for row in reader:
            try:
                row = cleanC1(row)
                writer.writerow(row)
            except IndexError:
                pass


class BiltHandler:
    """Handler for Bilt credit card statements."""
    
    @staticmethod
    def process(reader, writer, filename):
        """Process Bilt CSV data using legacy cleaning function."""
        for row in reader:
            try:
                row = cleanBilt(row)
                writer.writerow(row)
            except IndexError:
                pass
