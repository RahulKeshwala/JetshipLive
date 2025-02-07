from storages.backends.s3 import S3Storage




class staticFileStorage(S3Storage):
    #helpers.cloudflare.storage.staticFileStorage
    location='static'

class mediaFileStorage(S3Storage):
    #helpers.cloudflare.storage.mediaFileStorage
    location='media'    

