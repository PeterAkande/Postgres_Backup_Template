# Backup with Postgres pg_dump guide

#### Note: This assumes you are going to be taking these actions on a Linux machine

Let's create a high level demonstration of how things would work in the backup process.

We would be using the pg_dump and restore tool provided by Postgres.
For example, to create a backup of a DATABASE called EBAY_DB, we would do:
```commandline
pg_dump -U postgres_user EBAY_DB > DATABASE_DESTINATION_FILE.psql
```

While that works, it is a better practice to compress the backup as it can get quite large and that would eventually take up so much storage space.
So to backup using gzip, the commands becomes:

```commandline
pg_dump -U postgres_user EBAY_DB | gzip > DATABASE_DESTINATION_FILE.psql.gz
```
That creates a dump of the Database in text format.
To use Tar format(Recommended), the command becomes

```commandline
pg_dump -U postgres_user -F t EBAY_DB | gzip > DATABASE_DESTINATION_FILE.tar.gz
```

To automate this process so as not to always go through the stress of tping these into the terminal, we create a python script to 
run the command and create backup logs (For Debugging purposes).
An already created python script can be found with the name db_backup_script.py.

A cron job is then set up to run the python Script at intervals.

To set up the job, enter to the terminal:
```commandline
crontab -e
```
Then add the job to the file that must have been opened using nano or vim.
A sample cron job to run the python script at 1 min intervals is
```commandline
0-59 * * * *  /usr/bin/python3 /home/ubuntu/db_backup_script/db_backup_script.py
```
```0-59 * * * *```  basically Tells that the command ```/usr/bin/python3 /home/ubuntu/db_backup_script/db_backup_script.py``` should be
Executed every minute ```0-59``` of every hour ```*``` of every day of every week of every month.

[This is an excellent guide on cron jobs](https://www.freecodecamp.org/news/cron-jobs-in-linux/) by freecodecamp.
To generate the interval you can use [this tool](https://crontab.guru/).

# Uhmm Lets do a little bit about Restoring the DATABASE
To restore the Database, we are going to be using another tool from postgres pg_restore

But before we restore the database, lets first make sure that the databse has been created. We can just try to create it
If it hasnt been created, it gives us an error that can be ignored
```commandline
createdb -U postgres_user EBAY_DB
```

Now that the Db Exists, to restore the database EBAY_DB, we do

```commandline
pg_restore -U postgres_user -d EBAY_DB DATABASE_DESTINATION_FILE.psql
```

And if our file has been compressed using gzip, we can unzip the file using:
```commandline
gunzip DATABASE_DESTINATION_FILE.tar.gz
```

A simple Script do all these has been provided in the db_restore_script