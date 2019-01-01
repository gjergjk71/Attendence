from home.models import Facultys,Students
from rest_framework import serializers

class FacultysSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Facultys
		exclude = []


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Students
		exclude = []
