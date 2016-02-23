from fabric.api import task
import datetime

@task(alias='blp')
def backup_linkedin_prod():
  """
  Backup linkedin-prod mongodb
  """
  backup('linkedin_prod')

@task(alias='bp')
def backup_plugin():
  """
  Backup scraping-prod mongodb
  """
  backup('plugin')

@task(default=True)
def backup(server):

  if not server:
    return 1
  else:
    backup_folder_name = '%s-%s' % (server, datetime.date.today())
    print 'Backuping... %s - database name - %s' % (server, backup_folder_name)
    return 0

@task
def backup_two(server, db):
  print 'Backuping... %s - on server - %s' % (db, server)
