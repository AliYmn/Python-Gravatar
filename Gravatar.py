import hashlib

class Gravatar():
    """
    Gravatar işlemlerini sağlayan kütüphanedir.
    Gravatar class'ı tek parametre alır ve tek parametreye
    email adresini yolladığınız zaman size o email'e ait
    profil link çıktısı geri gönderir.
    :param : E-mail adress
    """
    def __init__(self,email):
        self.email = email

    def profile(self):
        """
        Yollanan email adresini profil link olarak geri gönderir.
        :return: profile
        """
        link = hashlib.md5(self.email.encode('utf-8')).hexdigest()
        profile = "http://www.gravatar.com/avatar/" + link
        return profile

if __name__ == '__main__':
    #from Gravatar import *
    # Example
    Gravatar_Profile = Gravatar('aliymn.db@gmail.com')
    print(Gravatar_Profile.profile())