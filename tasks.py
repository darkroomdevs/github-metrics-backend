import os
import sys

from invoke import task

python = sys.executable
sys.path.append('src')


#
# Call python manage.py in a more robust way
#
def manage(c, cmd, env=None, **kwargs):
    kwargs = {k.replace('_', '-'): v for k, v in kwargs.items() if v is not False}
    opts = ' '.join(f'--{k} {"" if v is True else v}' for k, v in kwargs.items())
    cmd = f'{python} manage.py {cmd} {opts}'
    env = {**os.environ, **(env or {})}
    path = env.get("PYTHONPATH", ":".join(sys.path))
    env.setdefault('PYTHONPATH', f'src:{path}')
    c.run(cmd, env=env)


#
# Django tasks
#
@task
def run(c, no_toolbar=False):
    """
    Run development server
    """
    env = {}
    if no_toolbar:
        env['DISABLE_DJANGO_DEBUG_TOOLBAR'] = 'true'
    else:
        manage(c, 'runserver 0.0.0.0:8000', env=env)


#
# DB management
#
@task
def db(c, migrate_only=False):
    """
    Perform migrations
    """
    if not migrate_only:
        manage(c, 'makemigrations')
    manage(c, 'migrate')


@task
def migrate(c):
    c.run('python manage.py migrate')


@task
def install(c):
    """
    Install all development dependencies
    """
    c.run('pip install -r requirements.txt')


@task
def travis(c):
    """
    Runs command that Travis CI runs
    """
    c.run('python playground.py')


@task
def create_admin(c):
    """
    Runs command that Travis CI runs
    """
    c.run('python manage.py createsuperuser2 --username test1 --password test1 --noinput --email "blank@email.com"')


@task
def playground(c):
    c.run('python playground.py')
