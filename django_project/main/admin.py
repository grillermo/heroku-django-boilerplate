from django.contrib import admin
from main.models import GenericModel

class GenericModelAdmin(admin.ModelAdmin):
    # list_display = ('id','first_name','last_name','username','added')
    # search_fields = ('first_name','last_name','username')
    # list_filter = ('recently_payed',)
    # ordering = ('-added',)
    # save_as = True
    
    def save_model(self,request,obj,form,change):
        # ''' Slugify slug just to be sure its done right '''
        # obj.slug_name = slugify(obj.slug_name)
        obj.save()
        pass
        
    class Media:
        # js = ( settings.ADMIN_MEDIA_PREFIX+'tinymce/jscripts/tiny_mce/tiny_mce.js',
        #        settings.ADMIN_MEDIA_PREFIX+"tinymce_setup/tinymce_setup.js",
        #              )
        pass
    
admin.site.register(GenericModel,GenericModelAdmin)
