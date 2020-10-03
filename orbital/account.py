from django.db.models.expressions import Random
from django.forms.widgets import PasswordInput
from .models import user,device
from hashlib import md5
'''
def hash_id(name, password):
    return md5(name+password)

class account():

    def __init__(self,user:user):
        self.__sql=user
    
    @property
    def Sql(self):
        return self.__sql

    def add_account(self,name, password,image_path)-> 'account':
        self.__mod_account__(name,password,image_path=None)
    
    def load_image(self,image_path):
        self.__add_immage__(image_path,save=True)

    def add_device(self,Device):
        
        pass

    def delate_device(self,Device):
        
        pass

    def modify_account(self,**user_kargs)-> 'account':
        def check_user_arg(a):
            if user_kargs[a]==self.Sql.objects.get(a) :
                tmp.setdefault(a,self.Sql.objects.get(a))
            else:
                tmp.setdefault(a,user_kargs[a])
        arg=['name','password']
        if self.search_account(**user_kargs) :
            tmp={}
            for a in arg:
                check_user_arg(a)
            self.__mod_account__(**tmp)

    def __mod_account__(self,**user_kargs):
        if user_kargs.__contains__('name') & user_kargs.__contains__('password') & user_kargs.__contains__('image_path'):
            name=user_kargs['name']
            password=user_kargs['password']
            self.__add_immage__(user_kargs['image_path'])
            tmp=self.__sql(name=name,password=password)
            tmp.save()
            
    def __search_account__(self,**user_kargs) -> bool:
        if user_kargs.__contains__('name') & user_kargs.__contains__('password'):
            obj=self.Sql.objects.filter(**user_kargs)
            if self.Sql.objects.__contains__(obj):
                return True
            else:
                return False
        return False

    def __add_immage__(self,image_path=None,save=False):
        if image_path is not None:
           self.__sql(image=image_path)
           if save:
               self.__sql.save()

    def __search_device__(self,Device,User_device:device)-> bool:
        if isinstance(User_device,device):
            if self.Sql.objects.__contains__(User_device):
                return User_device.objects.__contains__(Device)


    def __add_devce(self,Device,User_device:device,save=False):
        if isinstance(User_device,device):
            tmp_id=md5(Device)
            tmp=None
            if User_device.objects.count() != 0:
                tmp=self.Sql.objects.get('User_device')
            else:
                tmp=device(Device_name=Device,Id=tmp_id)
            self.__sql(User_device=tmp)
            if save:
               self.__sql.save()

    def __delate__device(self,Device,User_device:device):
        if self.__search_device__(Device,User_device):
            if User_device.objects.__contains__(Device):
                User_device.delete(Device)
        return User_device
'''

            


    



    

    
    
    