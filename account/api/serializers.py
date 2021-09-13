from rest_framework import serializers
from account.models import User
from account.validations import only_int


class UserSerializer(serializers.ModelSerializer):
    mobile_no = serializers.CharField(max_length=10, min_length=10, validators=[only_int])
    # is_staff = serializers.BooleanField(read_only=True, write_only=False)
    is_superuser = None
    updated_date = serializers.DateTimeField(read_only=True, write_only=False)

    class Meta:
        model = User
        # fields = ['first_name']
        # fields = '__all__'
        exclude = ('password', 'user_permissions', 'groups', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'first_name': {'required': True},
            'middle_name': {'required': True},
            'last_name': {'required': True},
            'mobile_no': {'required': True},
            'email': {'required': False},
        }

        def update(self, instance, validated_data):
            # instance.first_name = validated_data['first_name']
            # instance.save()
            return instance


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', "first_name", "middle_name", "last_name", "mobile_no", "country_code"]

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['password'])
        user.first_name = validated_data.get("first_name", "")
        user.last_name = validated_data.get("middle_name", "")
        user.last_name = validated_data.get("last_name", "")
        user.mobile_no = validated_data.get("mobile_no", "")

        if validated_data.get("country_code"):
            user.country_code = validated_data.get("country_code")

        user.save()
        return user
