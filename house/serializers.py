from rest_framework import serializers

from house.models import House


class HouseSerializer(serializers.ModelSerializer):
    manager = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name="profile-detail")
    members = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="profile-detail")
    members_count = serializers.IntegerField(read_only=True)
    taskLists = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="tasklist-detail", source="lists")

    class Meta:
        model = House
        fields = [
            "url", "id", "image", "name", "created_on",
            "manager", "description", "members_count", "members", "taskLists",
            "points", "completed_tasks_count", "not_completed_tasks_count",
        ]
        read_only_fields = ["points", "completed_tasks_count", "not_completed_tasks_count"]
