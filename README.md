# Python-Gravatar
Python üzerinde kullanabilceğiniz gravatar kütüphanesidir.

`Amac` : Kayıt olan kullanıcıların, profil resimlerini sunucuya yüklemeden gravatar üzerinden çekmenizi sağlayacaktır.

# Kurulum
  Ver : 1.0
  
  Python Ver : 3x
  
  NOT : Eğer python 2.7 ve 3x yüklü ise aşşağıdakileri sırayla giriniz.
  Sadece Python3 yüklü ise pip3'dekini kurmanız yeterli olacaktır.
  Ek bilgi : Windows kullaniyorsanız başındaki sudo etiketini kaldırın.
  
  `sudo pip install git+https://github.com/AliYmn/Python-Gravatar`
  
  `sudo pip3 install git+https://github.com/AliYmn/Python-Gravatar`

# Python-Gravatar Kullanımı

`import Gravatar`

` Gravatar_Python = Gravatar.Gravatar('aliymn.db@gmail.com')`

`Gravatar_Python_Profile =  Gravatar_Python.profile()`

` print('Gravatar_Python_Profile') `

`>>> http://www.gravatar.com/avatar/323fad61ec978a5b3425fbe56b06a101`


İşte Bukadar!
