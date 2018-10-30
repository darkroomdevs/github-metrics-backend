from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError


class Command(createsuperuser.Command):
    help = 'Crate a superuser, and allow password to be provided'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
                '--password', dest='password', default=None,
                help='Specifies the password for the superuser.',
        )
        parser.add_argument(
                '--preserve', dest='preserve', default=False, action='store_true',
                help='Exit normally if the user already exists.',
        )

    def handle(self, *args, **options):
        if not self.__process_options(**options):
            return
        super(Command, self).handle(*args, **options)
        self.__update_user(**options)

    def __process_options(self, **options):
        password = options.get('password')
        username = options.get('username')
        database = options.get('database')

        if password and not username:
            raise CommandError("--username is required if specifying --password")

        if username and options.get('preserve') \
                and self.UserModel._default_manager.db_manager(database).filter(username=username).exists():
            self.stdout.write("User exists, exiting normally due to --preserve")
            return False

        return True

    def __update_user(self, **options):
        password = options.get('password')
        username = options.get('username')
        database = options.get('database')

        if password:
            user = self.UserModel._default_manager.db_manager(database).get(username=username)
            user.set_password(password)
            user.save()
