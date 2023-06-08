from django.db import models
# Create your models here.


class Book(models.Model):
    img = models.ImageField(null=True, blank=True,
                            upload_to="static/images/products")
    name = models.CharField(max_length=200)
    price = models.FloatField()
    compare_at_price = models.FloatField()
    description = models.CharField(max_length=1000)
    estimate_ship_date = models.DateTimeField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class BookTag(models.Model):
    title = models.CharField(max_length=10)
    color = models.CharField(max_length=7)
    background = models.CharField(max_length=7)
    product = models.ForeignKey(
        Book, related_name="tags", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class BookThumnailImage(models.Model):
    alt = models.CharField(max_length=200)
    img = models.ImageField(null=True, blank=True,
                            upload_to="static/images/thumbnails")
    product = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='thumbnail_images', null=True)
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.imageURL


class BookImages(models.Model):
    alt = models.CharField(max_length=200)
    img = models.ImageField(null=True, blank=True,
                            upload_to="static/images/images")
    product = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='images', null=True)

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.imageURL