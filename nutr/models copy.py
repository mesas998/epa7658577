from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

"""
"FRS_FACILITY_DETAIL_REPORT_URL","REGISTRY_ID","PRIMARY_NAME","LOCATION_ADDRESS","SUPPLEMENTAL_LOCATION","CITY_NAME","COUNTY_NAME","FIPS_CODE","STATE_CODE","STATE_NAME","COUNTRY_NAME","POSTAL_CODE","FEDERAL_FACILITY_CODE","FEDERAL_AGENCY_NAME","TRIBAL_LAND_CODE","TRIBAL_LAND_NAME","CONGRESSIONAL_DIST_NUM","CENSUS_BLOCK_CODE","HUC_CODE","EPA_REGION_CODE","SITE_TYPE_NAME","LOCATION_DESCRIPTION","CREATE_DATE","UPDATE_DATE","US_MEXICO_BORDER_IND","PGM_SYS_ACRNMS","INTEREST_TYPES","NAICS_CODES","NAICS_CODE_DESCRIPTIONS","SIC_CODES","SIC_CODE_DESCRIPTIONS","LATITUDE83","LONGITUDE83","CONVEYOR","COLLECT_DESC","ACCURACY_VALUE","REF_POINT_DESC","HDATUM_DESC","SOURCE_DESC"

"""
class EPAColo(model.Models):
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
cdate = models.DateField()
udate = models.DateField()
mex = models.CharField(max_length=3)
abbrev = models.CharField(max_length=80)
eit = models.CharField(max_length=80)
naics = models.CharField(max_length=80)
ntext = models.CharField(max_length=80)
sic = models.CharField(max_length=80)
sict = models.CharField(max_length=80)
lat = models.DecimalField(max_digits=9,decimal_places=6)
long = models.DecimalField(max_digits=10,decimal_places=6)
conv = models.CharField(max_length=25)
hcmt = models.CharField(max_length=60)
ham = models.IntegerField()
rpn = models.CharField(max_length=40)
hrdn = models.CharField(max_length=5)
cdsn = models.CharField(max_length=35)
cbc = models.CharField(max_length=15)

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
        return reverse('nutr_nutrdef_delete',
                       kwargs={'slug': self.slug})
    
    def get_update_url(self):
        return reverse('nutr_nutrdef_update',
                       kwargs={'slug': self.slug})
    
    



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
