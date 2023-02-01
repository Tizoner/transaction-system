from rest_framework import serializers
from timezone_field import TimeZoneField
from timezone_field.choices import with_gmt_offset


class TimeZoneSerializerField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        super().__init__(
            with_gmt_offset(map(str, TimeZoneField.default_zoneinfo_tzs)), **kwargs
        )

    def to_representation(self, value):
        return str(super().to_representation(value))
