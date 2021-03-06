from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from model_utils import Choices

from us_states import STATE_CHOICES
from us_states import USPS_CHOICES


class USStateField(CharField):

    description = _("U.S. state (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = Choices(*STATE_CHOICES)
        kwargs['max_length'] = 2
        super(USStateField, self).__init__(*args, **kwargs)

class USPostalCodeField(CharField):

    description = _("U.S. postal code (two uppercase letters)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = Choices(*USPS_CHOICES)
        kwargs['max_length'] = 2
        super(USPostalCodeField, self).__init__(*args, **kwargs)

class PhoneNumberField(CharField):

    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from django.contrib.localflavor.us.forms import USPhoneNumberField
        defaults = {'form_class': USPhoneNumberField}
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)
