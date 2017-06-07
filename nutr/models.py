from django.core.urlresolvers import reverse
from django.db import models
class NutrDef(models.Model):
    nutr_no = models.IntegerField(db_index=True)
    slug = models.SlugField(
        max_length=3,
        unique=True,
        help_text='A label for URL config.')
    units = models.CharField(max_length=7)
    tagname = models.CharField(max_length=20)
    nutr_desc = models.CharField(max_length=60)
    num_dec = models.CharField(max_length=1)
    #r_order = models.IntegerField()
    class Meta:
        verbose_name = 'nutrient'
        ordering = ['-nutr_no']
        unique_together = ('slug',)
    def get_absolute_url(self):
        return reverse('nutr_nutrdef_detail',
                       kwargs={'slug': self.slug})
    def get_delete_url(self):
        pass

class NutData(models.Model):
    nutr_no = models.ForeignKey(NutrDef)
    ndb_no = models.CharField(max_length=5)
    nutr_val = models.DecimalField(max_digits=5,decimal_places=2)
    num_data_pts = models.IntegerField()
    std_error = models.DecimalField(max_digits=5,decimal_places=2)
    src_cd = models.CharField(max_length=2)
    deriv_cd = models.CharField(max_length=4)
    ref_ndb_no = models.CharField(max_length=5)
    add_nutr_mark = models.CharField(max_length=1)
    num_studies = models.IntegerField()
    min = models.DecimalField(max_digits=5,decimal_places=2)
    max = models.DecimalField(max_digits=5,decimal_places=2)
    df = models.CharField(max_length=1)
    low_eb = models.DecimalField(max_digits=5,decimal_places=2)
    up_eb = models.DecimalField(max_digits=5,decimal_places=2)
    stat_cmt = models.CharField(max_length=10)
    addmod_date = models.DateField()
    cc = models.CharField(max_length=1)
    def get_absolute_url(self):
        return reverse('nutr_nutrdef_detail',
                       kwargs={'nutr_no': self.nutr_no})

    def get_absolute_url(self):
        return reverse('nutr_nutdata_detail',
                       kwargs={'pk': self.pk})

class DataSrc(models.Model):
   datasrc_id = models.CharField(max_length=7,db_index=True)
   authors = models.CharField(max_length=255)
   title  = models.CharField(max_length=255)
   year  = models.CharField(max_length=4)
   journal  = models.CharField(max_length=135)
   vol_city  = models.CharField(max_length=16)
   issue_state  = models.CharField(max_length=5)
   start_page  = models.CharField(max_length=5)
   end_page  = models.CharField(max_length=5)

class Datsrcln (models.Model):
    nutr_no = models.ForeignKey(NutData)
    ndb_no = models.CharField(max_length=5)
    datasrc_id = models.ForeignKey(DataSrc)

class EPAColo(models.Model):
    ffdru = models.CharField(max_length=63)
    fregid = models.CharField(max_length=12)
    fsn = models.CharField(max_length=80)
    lat = models.CharField(max_length=50)
    slt = models.CharField(max_length=50)
    loc = models.CharField(max_length=60)
    county = models.CharField(max_length=35)
    fips = models.CharField(max_length=5)
    usps = models.CharField(max_length=2)
    state = models.CharField(max_length=35)
    country = models.CharField(max_length=44)
    postal = models.CharField(max_length=14)
    ffic = models.CharField(max_length=50)
    fan = models.CharField(max_length=50)
    tribe = models.CharField(max_length=3)
    tln = models.CharField(max_length=80)
    cdn = models.CharField(max_length=2)
    huc = models.CharField(max_length=8)
    region = models.CharField(max_length=2)
    type = models.CharField(max_length=40)
    desc = models.CharField(max_length=80)
    cdate = models.CharField(max_length=10)
    udate = models.CharField(max_length=10)
    mex = models.CharField(max_length=3)
    abbrev = models.CharField(max_length=80)
    eit = models.CharField(max_length=80)
    naics = models.CharField(max_length=80)
    ntext = models.CharField(max_length=80)
    sic = models.CharField(max_length=80)
    sict = models.CharField(max_length=80)
    lati = models.CharField(max_length=10)
    long = models.CharField(max_length=10)
    conv = models.CharField(max_length=25)
    hcmt = models.CharField(max_length=60)
    ham = models.CharField(max_length=3)
    rpn = models.CharField(max_length=40)
    hrdn = models.CharField(max_length=5)
    cdsn = models.CharField(max_length=35)
    cbc = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('nutr_epacolo_detail',
                       kwargs={'ffdru': self.ffdru})
