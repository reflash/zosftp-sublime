from ftplib import FTP
import ftplib
import json
import re
import os
import time
import ntpath


#
#   z_OS_FTP_Client functions
#
#   submit_job(self,filename) - this function does submit 
#   a file as a  job and does nothing else
#
#   submit_job_and_wait(self,filename) - this function submits a file as a job, 
#   waits when it ends and returns the results
#
#   open_dataset(self, dataset_name) - this function opens file from mainframe 
#   and returns resulting list
#
#   save_dataset(self, filepath, dataset_name) - this function saves file
#   on a remote host
#
#   Settings class must contain host, login and password fields


class z_OS_FTP_Client(object):

    settings = None
    ftp = None

    def __init__(self,settings):
        self.settings = settings
        self.ftp = FTP(settings.host)
        self.ftp.login(settings.login, settings.password)


    # API Functions    
    def submit_job(self,filepath):
        
        self.ftp.sendcmd("site FILEType=JES JESJOBNAME=* JESOWNER=*")

        return self.ftp.storlines("STOR " + ntpath.basename(filepath), 
            open(filepath,'rb'))

    def submit_job_and_wait(self,filepath):

        response = self.submit_job(filepath)
        job_id = self.parse_job_id(response)
        result = self.wait_result(job_id)

        return result

    def open_dataset(self, dataset_name):

        result = []
        
        self.ftp.retrlines("RETR '" +dataset_name+ "'",
                lambda line : result.append(line + "\n"))

        return result

    def save_dataset(self, filepath, dataset_name):

        self.ftp.storlines("STOR '" +dataset_name+ "'",
                open(filepath,'rb'))



    # Utility Functions
    def parse_job_id(self,text):

        pattern = r"250-It is known to JES as (.+)"
        regex = re.compile(pattern)
        result = regex.match(text)
        return result.group(1)

    def wait_result(self,id):

        spool = []
        success = False;
        tries = 0

        while not(success) and tries < 5:
            try:
                self.ftp.retrlines("RETR " + id,
                    lambda line : spool.append(line + "\n"))
                success = True
            except ftplib.all_errors as ex:
                print("Waiting..." + id)
                tries += 1

        return spool