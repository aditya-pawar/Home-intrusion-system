import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config( 
  cloud_name = "aditya1510", 
  api_key = "938822388331429", 
  api_secret = "ETfu1XNHqmbO2pxBPB8AwH0oGcw" 
)
result = cloudinary.uploader.upload("/home/aditya/1.jpg")
print result
