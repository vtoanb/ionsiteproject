from django.contrib import admin
from .models import carousel,event,Film_link,Website_caption,Contact_info,FAQ,Visiter_message
from django.db import models
from django.forms import TextInput, Textarea
#from .widgets import RichTextEditorWidget
from django import forms
# Register your models here.
class eventFlatAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Event name', {
            'fields': ('event_name',)
        }),
        ('Event Description', {
            'classes': ('collapse',),
            'fields': ('event_text',),
        }),
        ('Event Picture',{
            'classes': ('collapse',),
            'fields': ('event_pic',),
        })
    )
    list_display = ('event_name',)
    
class carouselAdmin(admin.ModelAdmin):
    list_display = ('carousel_header',)
    
""" Create admin for Website_caption
    Use forms.ModelForm to change textarea for some fields
"""
class CaptionForm(forms.ModelForm):
    Event_part_caption = forms.CharField(widget = forms.Textarea)
    Film_part_caption = forms.CharField(widget = forms.Textarea)
    Marketing_part_caption = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Website_caption
        fields = ('Event_part_caption','Film_part_caption','Marketing_part_caption',)
        
class CaptionAdmin(admin.ModelAdmin):
    form = CaptionForm
    
""" Admin site for FAQ """
class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = FAQ
        fields = ('question','answer',)
        
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    
""" Admin site for Visiter_message """
class VisiterForm(forms.ModelForm):
    note = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = Visiter_message
        fields = ('name','email','note',)
        
class VisiterAdmin(admin.ModelAdmin):
    readonly_fields = ('name','email','note',)
    form = VisiterForm
    
    
admin.site.register(carousel,carouselAdmin)
admin.site.register(event,eventFlatAdmin)
admin.site.register(Website_caption,CaptionAdmin)
admin.site.register(Contact_info)
admin.site.register(Film_link)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(Visiter_message,VisiterAdmin)