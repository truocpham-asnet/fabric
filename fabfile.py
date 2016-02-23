from fabric.api import *
from fabric.contrib.console import *
from backup import *
from deploy import *

@task
def run():
  '''
  Main fabric run
  '''

  print 'Expose here!'

  backup_res = backup(None)

  if backup_res == 0:
    print 'Backup succeed %s' % backup_res
  else:
    print 'Backup failure %s' % backup_res
    confirm('Are you sure to continue?', default=True)
    full_deploy()