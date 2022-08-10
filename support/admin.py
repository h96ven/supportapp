from django.contrib import admin

from support.models import Reply, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    actions = ('batch_set_status_to_solved',)
    list_display = ('topic', 'updated_at', 'status', 'user')
    list_editable = ('status',)
    list_filter = ('user', 'updated_at', 'status')
    list_per_page = 10
    search_fields = ('topic__istartswith',)
    readonly_fields = ('user',)

    # Adding an action for setting status of multiple entries to Solved
    @admin.action(description='Set status to Solved')
    def batch_set_status_to_solved(self, request, queryset):
        updated_count = queryset.update(status=Ticket.STATUS_SOLVED)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated!'
        )


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'text', 'date')
    list_per_page = 10
    readonly_fields = ('user',)

    # Auto populating user field with current user
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
