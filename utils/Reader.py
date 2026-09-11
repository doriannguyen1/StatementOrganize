"""Main CSV reader that routes to card-specific handlers."""

import csv
import os

from utils.handlers.AllyHandler import AllyHandler
from utils.handlers.AmexHandler import AmexHandler
from utils.handlers.C1VentureHandler import C1VentureHandler
from utils.handlers.ChaseHandler import ChaseHandler
from utils.handlers.LegacyHandlers import BiltHandler, C1Handler


class Reader:
    """Main orchestrator for processing bank/credit card statements."""
    
    def read(self, filename):
        """Process a CSV file and route to appropriate handler."""
        lname = filename.lower()
        input_filename = 'input/' + filename
        output_filename = 'output/' + filename
        
        print(input_filename)
        os.makedirs('output', exist_ok=True)
        
        with open(input_filename, newline='') as csvfile, \
             open(output_filename, 'w', newline='') as outfile:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(outfile, delimiter=',')
            
            # Route to appropriate handler based on filename
            if "c1 venture" in lname or "venture" in lname or "transaction_download" in lname:
                C1VentureHandler.process(reader, writer, filename)
            elif "c1" in lname:
                C1Handler.process(reader, writer, filename)
            elif "chase" in lname:
                ChaseHandler.process(reader, writer, filename)
            elif "bilt" in lname:
                BiltHandler.process(reader, writer, filename)
            elif "amex" in lname or "activity" in lname:
                AmexHandler.process(reader, writer, filename)
            elif "ally" in lname or "transactions" in lname:
                AllyHandler.process(reader, writer, filename)
