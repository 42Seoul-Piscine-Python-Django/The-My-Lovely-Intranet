from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User, PostModel, CommentModel, ProfileModel


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'name', 'surname', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('id', 'email', 'password')}),
        ('Personal info', {
         'fields': ('profile_image', 'name', 'surname', 'description')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id', 'email', 'profile_image', 'name', 'surname', 'password1', 'password2')}
         ),
    )
    search_fields = ('id', 'email',)
    ordering = ('id', 'email',)
    filter_horizontal = ()


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'active', 'parent', 'post', 'comment')
    list_filter = ('active', 'creationDate', 'updateDate')
    search_fields = ('author', 'comment')


class PostCommentAdmin(admin.StackedInline):
    model = CommentModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'creationDate', 'updateDate')
    list_filter = ('creationDate', 'updateDate', 'author')
    search_fields = ('title', 'content')
    inlines = (PostCommentAdmin, )

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')
    list_filter = ('id', 'email', 'name')
    search_fields = ('id', 'email')

admin.site.register(ProfileModel)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
