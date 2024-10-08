from rest_framework import serializers

from house.models import House
from task.models import TaskList, Task, Attachment


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name="profile-detail")
    completed_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name="profile-detail")
    task_list = serializers.HyperlinkedRelatedField(queryset=TaskList.objects.all(), many=False,
                                                    view_name="tasklist-detail")
    attachments = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="attachment-detail")

    def validate_task_list(self, value):
        user_profile = self.context['request'].user.profile
        if value not in user_profile.house.lists.all():
            raise serializers.ValidationError("Tasklist provided does not belong to the house for which the user is a member.")
        return value

    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        task = Task.objects.create(**validated_data)
        task.created_by = user_profile
        task.save()
        return task

    class Meta:
        model = Task
        fields = [
            "url", "id", "name", "description", "attachments",
            "status", "created_on", "completed_on",
            "created_by", "completed_by", "task_list"
        ]
        read_only_fields = ["created_on", "created_by", "completed_on", "completed_by", "status"]


class TaskListSerializer(serializers.ModelSerializer):
    house = serializers.HyperlinkedRelatedField(queryset=House.objects.all(), many=False, view_name="house-detail")
    created_by = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name="profile-detail")
    tasks = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name="task-detail")
    # tasks = TaskSerializer(read_only=True, many=True)

    def validate_house(self, value):
        user_profile = self.context['request'].user.profile
        print(value)
        print(user_profile.house)
        if value != user_profile.house:
            raise serializers.ValidationError("You do not belong to the house provided.")
        return value

    def create(self, validated_data):
        user_profile = self.context['request'].user.profile
        task_list = TaskList.objects.create(**validated_data)
        task_list.created_by = user_profile
        task_list.save()
        return task_list

    class Meta:
        model = TaskList
        fields = [
            "url", "id", "name", "description", "tasks",
            "status", "created_on", "house", "created_by",
        ]
        read_only_fields = ["created_on", "status"]


class AttachmentSerializer(serializers.ModelSerializer):
    task = serializers.HyperlinkedRelatedField(queryset=Task.objects.all(), many=False, view_name="task-detail")

    def validate_task(self, value):
        user_profile = self.context['request'].user.profile
        task = value
        task_list = TaskList.objects.get(tasks__id__exact=task.id)
        if task_list not in user_profile.house.lists.all():
            raise serializers.ValidationError("Task provided does not belong to the house for which the user is a member.")
        return value

    class Meta:
        model = Attachment
        fields = ["url", "id", "created_on", "data", "task"]
        read_only_fields = ["created_on"]
