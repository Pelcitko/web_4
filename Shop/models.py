from django.db import models
from django.db.models import URLField
from django.utils import timezone
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    new_rose = instance.__class__.objects.order_by("id").last()
    var = instance.of_rose
    new_id = new_rose.id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "img/%s/%s_%s" % (var, new_id, filename)


class RoseImage(models.Model):
    of_rose = models.ForeignKey('Rose', verbose_name='Růže', on_delete=models.CASCADE)
    image = ImageField(upload_to=upload_location,
                      null=True, blank=True,
                      width_field="width_field",
                      height_field="height_field")
    height_field = models.IntegerField(default=230)
    width_field = models.IntegerField(default=320)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'obrázek'
        verbose_name_plural = 'obrázky'


class Color(models.Model):
    name = models.CharField('Barva', max_length=32)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Barva'
        verbose_name_plural = 'Barvy'


class Country(models.Model):
    name = models.CharField('Národnost', max_length=20)
    shortcut = models.CharField('Zkratka státu', max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Národnost'
        verbose_name_plural = 'Národnost'


class Price(models.Model):
    price = models.PositiveSmallIntegerField('Cenova skupina', default=120)

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Cena'
        verbose_name_plural = 'Cenové skupiny'


class Section(models.Model):
    name = models.CharField('Skupina', max_length=21)
    description = RichTextField('Popis', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skupina'
        verbose_name_plural = 'Skupiny růží'


class Breeder(models.Model):
    name = models.CharField('Jmeno', max_length=64)
    description = models.TextField('Poznámka', blank=True)
    url = URLField(blank=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True) #+null

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Šlechtitel'
        verbose_name_plural = 'Šlechtitelé'


class Honor(models.Model):
    name = models.CharField('Ocenění', max_length=20)
    description = RichTextField('Popis', blank=True)
    # ico

    def __str__(self):
        return self.name


CHOICES =(
    (1, 'Málo'),
    (2, 'Trochu'),
    (3, 'Středně'),
    (4, 'Hodně'),
)


class Rose(models.Model):
    name = models.CharField('Název', max_length=70)
    img = models.ForeignKey(
        'RoseImage', verbose_name='náhled růže', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.ForeignKey(
        'Price', verbose_name='Cena', on_delete=models.SET_NULL, null=True, blank=True)
    add_price = models.SmallIntegerField('Přidaná cena', default=0)
    color = models.ManyToManyField('Color', verbose_name='Barva')
    flower_size = models.PositiveSmallIntegerField('Velikost květu', null=True)
    flower_kind = models.CharField('Typ květu', max_length=70, null=True)
    section = models.ManyToManyField('Section', verbose_name='Skupina')
    breeder = models.ForeignKey(
        'Breeder', verbose_name='Šlechtitel', on_delete=models.SET_NULL, null=True, blank=True)
    honor = models.ForeignKey(
        'Honor', verbose_name='Ocenění', on_delete=models.SET_NULL, null=True, blank=True)
    year = models.PositiveSmallIntegerField('Rok', blank=True, null=True)
    # If you are using this field with MySQLdb 1.2.2 and the utf8_bin
    description = models.TextField('Krátký popisek', blank=True)
    text = RichTextField('Popis růže', blank=True)
    added_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField('date published')
    plants_per_m2 = models.SmallIntegerField('Na m2', blank=True, null=True)
    distance = models.PositiveSmallIntegerField(
        'Rozestupy', blank=True, null=True)
    height = models.PositiveSmallIntegerField('Výška od', null=True)
    max_height = models.PositiveSmallIntegerField(' do', blank=True, null=True)
    width = models.PositiveSmallIntegerField('Šířka od', null=True)
    max_width = models.PositiveSmallIntegerField(' do', blank=True, null=True)
    growth_habit = models.CharField('Tvar keře', max_length=70, blank=True)
    add_info = models.CharField('Další informace', max_length=300, blank=True)
    fragrance = models.PositiveSmallIntegerField(
        'Vůně', choices=CHOICES, null=True)
    # petal count
    hardiness = models.PositiveSmallIntegerField(
        'Mrazuvzdornost', choices=CHOICES, null=True)
    black_spot = models.PositiveSmallIntegerField(
        'Černá skvrnitost', choices=CHOICES, null=True)
    mildew = models.PositiveSmallIntegerField(
        'Padlí', choices=CHOICES, default=3)

    class Meta:
        verbose_name = 'Růže'
        verbose_name_plural = 'Růže'
        ordering = ["-name", "-honor"]

    def publish(self):
        self.published_date = timezone.datetime.today()
        self.save()

    def __str__(self):
        return self.name

    def __iter__(self):
        return [field.value_to_string(self) for field in Rose._meta.fields]


class Stock(models.Model):
    rose = models.ForeignKey('Rose', on_delete=models.SET_NULL, null=True) #+null
    year = models.PositiveSmallIntegerField('Rok', default=timezone.now().year)
    spring = models.BooleanField('Jaro', default=False)
    rose_count = models.PositiveSmallIntegerField(
        'Na skladě', blank=True, null=True)
    loose_count = models.PositiveSmallIntegerField(
        'Dvojek', blank=True, null=True)
    grow = models.PositiveSmallIntegerField('Ujmulo se', blank=True, null=True)
    implant = models.PositiveSmallIntegerField('Očkováno', null=True)

    class Meta:
        verbose_name = 'Sklad'
        verbose_name_plural = 'Sklady'
        unique_together = (("rose", "year", "spring"),)

    def __str__(self):
        return str(self.rose_count) + ' / ' + str(self.implant)


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name='Uživatel')
    info = models.TextField('Poznámka', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profil'
        verbose_name_plural = 'profily'


class Cart(models.Model):
    rose = models.ForeignKey('Rose', on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField('Rok', default=timezone.now().year)
    spring = models.BooleanField('Jaro', default=False)
    rose_count = models.PositiveSmallIntegerField(
        'Na skladě', blank=True, null=True)
    loose_count = models.PositiveSmallIntegerField(
        'Dvojek', blank=True, null=True)
    grow = models.PositiveSmallIntegerField('Ujmulo se', blank=True, null=True)
    implant = models.PositiveSmallIntegerField('Očkováno', null=True)

    class Meta:
        verbose_name = 'Sklad'
        verbose_name_plural = 'Sklady'
        unique_together = (("rose", "year", "spring"),)

    def __str__(self):
        return str(self.rose_count) + ' / ' + str(self.implant)
