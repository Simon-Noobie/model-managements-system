from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class RestrictedAccessMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return self.request.method in ['GET', 'POST']

    def handle_no_permission(self):
        raise PermissionDenied("You don't have to access this page.")