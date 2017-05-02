from crontab import CronTab
import os
myUser = os.path.expanduser("~/test.py")
# get rid of the home/
myUser = myUser[6:]
# find the ind of the back part of /
ind = myUser.find('/')
# gets the whole username
myUser = myUser[:ind]
tab = CronTab(user=myUser)
cmd = 'python /home/nathan/test.py'
cron_job = tab.new(cmd, comment='virus')
cron_job.minute.every(1)
tab.write()

