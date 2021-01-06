from datetime import datetime
import os

directory = os.getcwd()
timestamp = datetime.now().strftime("(%d/%m/%Y %H:%M:%S)")

def add_to_log():
    
    with open(f'{directory}/file.log', 'a') as log:
        print(timestamp, 
            'fetched & sent',
            file=log,
            end='\n')