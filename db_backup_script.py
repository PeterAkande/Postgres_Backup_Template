# This would run a script to backup the post gres database at intervals
# Run this in the terminal crontab -e
# It would open a file in vim editor
# Add this to the cron file 0 * * * * {pyhon_location} {this_file_location}

# The python location can be gotten by running $which python
# this_file_location is the directory that this file was stored in. Make it absolute not relative.

# ALL PATHS SHOULD BE ABSOLUTE AND NOT RELATIVE.

import os
from datetime import datetime
from pathlib import Path

current_file_path = Path(__file__).resolve().parent

#  Now Run The command
f = open(os.path.join(current_file_path, 'backup_logs.txt'), 'a')
current_date = datetime.now()  # Get the current name
current_date_as_command_line_safe = str(current_date).replace(' ', '__')

f.write(f'\nStarting Backup on {current_date_as_command_line_safe}\n')

DATABASE_NAME: str = "dvdrentals"  # This is the database name you used when you created the postgres database
OUTPUT_DIRECTORY: str = '/home/ubuntu/post_gres_library_backups'  # This is the directory with which the file backup would be written to.
OUTPUT_DATABASE_NAME: str = 'library_backup'  # This is the name with which the file is to be stored as.
POSTGRES_USER: str = 'peter'  # This is the username of the user that can

DATABASE_BACKUP_DESTINATION = os.path.join(OUTPUT_DIRECTORY,
                                           f"{OUTPUT_DATABASE_NAME}_{current_date_as_command_line_safe}")

# This would store the the database file in the file of name format OUTPUT_DATABASE_NAME_2023-28-06 10:12:222
commmand = f"pg_dump -U {POSTGRES_USER} -F t {DATABASE_NAME}| gzip  > {DATABASE_BACKUP_DESTINATION}.tar.gz"
f.write(f'Running Command. "{commmand}"\n')

return_code = os.system(commmand)  # This is okay, No need to use the subprocess module

print(f"The Backup Finished with status code {return_code}\n")
f.write(f'Backup Finished with Status code {return_code}\n')
f.write('========================================================== \n')

f.close()
