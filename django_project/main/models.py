from django.db import models

class GenericModel(models.Model):
    '''
    Docs
    '''
    pass

    def __unicode__(self):
        return u''

    def save(self,*args,**kwargs):
        '''
        '''
        super(GenericModel, self).save(*args, **kwargs) 
                    
    class Meta:
        # ordering = ['last_modified']
        # verbose_name = u'Generic'
        # verbose_name_plural = u'Generics'
        pass


# Create your models here.
