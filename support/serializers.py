from rest_framework import serializers

from support.models import Reply, Ticket


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id', 'date', 'text', 'user')
        read_only_fields = ('user',)

    def create(self, validated_data):
        ticket_id = self.context['ticket_id']

        return Reply.objects.create(
                ticket_id=ticket_id, **validated_data)


class TicketSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, required=False)

    class Meta:
        model = Ticket
        fields = (
            'id', 'topic', 'message', 'replies',
            'created_at', 'updated_at', 'status', 'user')
        read_only_fields = ('user',)
