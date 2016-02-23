from fabric.api import task

@task
def migrate():
    print 'Migrate process'

@task
def push():
    print 'Push process'

@task
def provision():
    print 'Install provision'

@task(default=True)
def full_deploy():
    provision()
    push()
    migrate()