#-*- coding: utf-8 -*-
import hashlib

"""gravatar.com üzerinden, mail üzerinden profil url bilgisini almaya yarayan modüldür."""

class GravatarInfo():
    """
    # Arguments #
    url:email()         | String formatında email adres bilgisi almaktadır.
    # Properties #
    url:email()         | İstekte bulunan email, gravatar.com üzerinden taranır ve bilgiler verilir.
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
    # Example

    gravatar_email = GravatarInfo("aliymn.db@gmail.com")

    gravatar_url = gravatar_email.profile()

    print(gravatar_url)