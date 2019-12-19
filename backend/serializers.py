from rest_framework import serializers

from backend.models import Member, Habit, Type


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = '__all__'

    def get_member(self, obj):
        return obj.member.first_name + ' ' + obj.member.last_name if obj.member else ''

    def get_type(self, obj):
        return obj.type.name if obj.type else ''


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
