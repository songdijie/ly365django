"""
# user.py.

# do the init for user
"""

from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    """
    UserInfo class implent.

    property:
    """

    user = models.OneToOneField(
        User, related_name='user', on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    avatar = models.FileField(null=True, blank=True)

    def __str__(self):
        """__str__."""
        return "phone %s" % self.phone
