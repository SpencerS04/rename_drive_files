## Script to Rename Files in my Google Drive

This is just a simple python script that does what the title suggests.
It will loop through every file in a Google Drive, replace all spaces and hyphens with underscores, and make all files lowercase.

It uses the (now depricated) wrapper library ![https://github.com/googlearchive/PyDrive](PyDrive), that makes interfacing with Google Drive's API super easy.
If you are for some reason copying this script, remember to add your own Google API information in a client_secrets.json file.
