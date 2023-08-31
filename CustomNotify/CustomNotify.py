from __future__ import absolute_import
from Deadline.Scripting import RepositoryUtils, PathUtils
from Deadline.Events import DeadlineEventListener
from Deadline.Events import *
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def GetDeadlineEventListener():
    return CustomNotify()


def CleanupDeadlineEventListener(deadlinePlugin):
    """This is the function that Deadline calls when the event plugin is
    no longer in use so that it can get cleaned up.
    """
    deadlinePlugin.Cleanup()


def SendMail(mail_msg, smtp_data):

    message = MIMEMultipart("alternative")
    message["Subject"] = mail_msg["subject"]
    message["From"] = mail_msg["sender"]
    message["To"] = mail_msg["receiver"]
    
    message.attach(MIMEText(mail_msg["body"], mail_msg["type"]))
    
    try: 
    
        with smtplib.SMTP(smtp_data["server"], smtp_data["port"]) as server:
            server.starttls()
            server.login(smtp_data["account"], smtp_data["token"])
            server.sendmail(mail_msg["sender"], mail_msg["receiver"], message.as_string())
            server.quit()
    
    except:
        self.LogInfo("CustomNotify: There was an error sending email. Check your SMTP settings.")
        raise Exception("CustomNotify: There was an error sending email. Check your SMTP settings.")

class CustomNotify(DeadlineEventListener):
    
    def __init__( self ):
        if sys.version_info.major == 3:
            super().__init__()
            
        # Set up the event callbacks here
        self.OnJobSubmittedCallback += self.OnJobSubmitted
        self.OnJobFinishedCallback += self.OnJobFinished
        self.OnJobStartedCallback += self.OnJobStarted
        self.OnJobFailedCallback += self.OnJobFailed
        self.OnJobResumedCallback += self.OnJobResumed
        self.OnJobSuspendedCallback += self.OnJobSuspended
        self.OnJobErrorCallback += self.OnJobError

        
    def Cleanup(self):
        del self.OnJobSubmittedCallback
        del self.OnJobFinishedCallback
        del self.OnJobStartedCallback
        del self.OnJobFailedCallback
        del self.OnJobResumedCallback
        del self.OnJobSuspendedCallback
        del self.OnJobErrorCallback

    def OnJobSubmitted(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgSubmitted", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgSubmittedSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify: Notifying of job {jobname} submission".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
        

    def OnJobStarted(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgStarted", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgStartedSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify:Notifying of job {jobname} start".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
        

    def OnJobFinished(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgCompleted", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgCompletedSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify:Notifying of job {jobname} completion".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
        
        
    def OnJobFailed(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgFailed", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgFailedSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify: Notifying of job {jobname} failure".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
        
        
    def OnJobResumed(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgResumed", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgResumedSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify: Notifying of job {jobname} resume".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
        
        
    def OnJobSuspended(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgSuspended", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgSuspendedSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify: Notifying of job {jobname} suspense".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
       
        
    def OnJobError(self, job):
        msg = {}
        smtp = {}
        smtp["account"] = self.GetConfigEntryWithDefault("SmtpAccount", "")
        smtp["token"] = self.GetConfigEntryWithDefault("SmtpToken", "")
        smtp["server"] = self.GetConfigEntryWithDefault("SmtpHostname", "")
        smtp["port"] = self.GetIntegerConfigEntryWithDefault("SmtpPort", 587)       
        msg["type"] = self.GetConfigEntryWithDefault("MsgType", "text")
        msg["sender"] = self.GetConfigEntryWithDefault("SenderEmail", "")
        msg["receiver"] = self.GetConfigEntryWithDefault("ReceiverEmail", "")
        msg["body"] = self.GetConfigEntryWithDefault("MsgError", "").format(jobname = "\"" + job.JobName + "\"") 
        msg["eol"] = "\n" if msg["type"] == "plain" else "<br>"
        msg["body"] = msg["body"].replace(";", msg["eol"])
        msg["subject"] = self.GetConfigEntryWithDefault("MsgErrorSubj", "").format(jobname = "\"" + job.JobName + "\"") 
                
        self.LogInfo("CustomNotify: Notifying of job {jobname} error".format(jobname = "\"" + job.JobName + "\""))
        SendMail(msg, smtp)
