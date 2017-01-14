# Python-Gravatar
Python üzerinde kullanabilceğiniz gravatar kütüphanesidir.

`Amac` : Kayıtlı olan kullanıcıların, profil resimlerini sunucuya yüklemeden gravatar üzerinden çekmenizi sağlayacaktır.

# Kurulum

    pip install git+https://github.com/AliYmn/Python-Gravatar

# Python-Gravatar Kullanımı

Gravatar paketini modülünü, yüklediğimize göre ekleyebiliriz.

    from gravatar import GravatarInfo

#Örnek Kullanımı

    from gravatar import GravatarInfo

    gravatar_email = GravatarInfo("aliymn.db@gmail.com")

    gravatar_url = gravatar_email.profile()

    print(gravatar_url)
    
 **ÇIKTI ;**

    http://www.gravatar.com/avatar/323fad61ec978a5b3425fbe56b06a101