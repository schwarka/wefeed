import os

import django
import dotenv

dotenv.read_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wefeed.settings")

django.setup()

from django.contrib.auth import get_user_model  # noqa
from django.contrib.auth.models import Group  # noqa

INITIALIZE = os.environ.get("INITIALIZE", False)

if INITIALIZE:
    print("Initializing")
    User = get_user_model()

    try:
        admin_user = User.objects.create_superuser(
            "admin", "rzwink@gmail.com", os.environ.get("INIT_PASS")
        )
    except django.db.utils.IntegrityError:
        pass

    groups_list = [
        "volunteer",
        "provider",
        "consumer",
        "operator",
    ]
    for name in groups_list:
        try:
            group, created = Group.objects.get_or_create(name=name)
        except django.db.utils.IntegrityError:
            pass
