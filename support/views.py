from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Reply, Ticket
from .permissions import IsOwner
from .serializers import ReplySerializer, TicketSerializer


class TicketViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    # Giving the current user permissions to see list view of
    # only the objects he owns.
    def get_queryset(self):
        return Ticket.objects.all().filter(user=self.request.user.id)

    # Auto populate user field by the current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReplyViewSet(ModelViewSet):
    serializer_class = ReplySerializer

    '''By adding the next two methods we exclude replies
    that don't belong to that particular ticket. For example,
    in url tickets/3/replies/ we only see replies for ticket 3.
    And without these methods we see all replies from all
    tickets in any ticket.
    '''
    def get_queryset(self):
        return Reply.objects.filter(ticket_id=self.kwargs['ticket_pk'])

    def get_serializer_context(self):
        return {'ticket_id': self.kwargs['ticket_pk']}

    # Auto populate user field by current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
