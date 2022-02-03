from django.db import models



class StoreMasterModel(models.Model):
  
##################### SP_GENERATE_DATA {}
  ASOFDATE=models.CharField(max_length=50,null=True,blank=True)
  COMPCODE=models.CharField(max_length=5,null=True,blank=True)
  SITECODE=models.CharField(primary_key=True, max_length=5)
  STOREDESC=models.CharField(max_length=50,null=True,blank=True)
  MALLNAME=models.CharField(max_length=50,null=True,blank=True)
  TELP=models.CharField(max_length=30,null=True,blank=True)
  EMAIL=models.CharField(max_length=30,null=True,blank=True)
  CONCEPT=models.CharField(max_length=30,null=True,blank=True)
  PROVINCE=models.CharField(max_length=30,null=True,blank=True)
  REGIONAL=models.CharField(max_length=30,null=True,blank=True)
  GM_OM=models.CharField(max_length=30,null=True,blank=True)
  GM_MAIL=models.CharField(max_length=30,null=True,blank=True)
  OM_NAME=models.CharField(max_length=30,null=True,blank=True)
  OM_MAIL=models.CharField(max_length=30,null=True,blank=True)
  OM_PHONE=models.CharField(max_length=30,null=True,blank=True)
  OIC_NAME=models.CharField(max_length=30,null=True,blank=True)
  OIC_MAIL=models.CharField(max_length=30,null=True,blank=True)
  OIC_PHONE=models.CharField(max_length=30,null=True,blank=True)
  SBU=models.CharField(max_length=5,null=True,blank=True)
  STORETYPE=models.CharField(max_length=10,null=True,blank=True)
  SITEPROFILE=models.CharField(max_length=20,null=True,blank=True)
  CONNECTION_TYPE=models.CharField(max_length=20,null=True,blank=True)
  STORESTATUS_SQL=models.CharField(max_length=20,null=True,blank=True)
  STOREOPEN_DATE=models.CharField(max_length=20,null=True,blank=True)
  STORECLOSE_DATE=models.CharField(max_length=20,null=True,blank=True)
  FAILOVER_STATUS=models.CharField(max_length=20,null=True,blank=True)
  JASPER_NUMBER_DEVICE=models.CharField(max_length=20,null=True,blank=True)
  JASPESR_DEVICE=models.CharField(max_length=20,null=True,blank=True)
  JASPER_IPADDRESS=models.CharField(max_length=20,null=True,blank=True)
  JASPER_MSISDN=models.CharField(max_length=20,null=True,blank=True)
  JASPER_IMSI=models.CharField(max_length=20,null=True,blank=True)
  ROOT_STATUS=models.CharField(max_length=20,null=True,blank=True)
  IP_EXTERNAL=models.CharField(max_length=20,null=True,blank=True)
  IP_MIKROTIK=models.CharField(max_length=20,null=True,blank=True)
  IP_GATEWAY=models.CharField(max_length=20,null=True,blank=True)
  IP_FORTIGATE=models.CharField(max_length=20,null=True,blank=True)



class ServerListModel(models.Model):
 #primary_key=True, max_length=5)
  Server_Status =models.CharField(max_length=50,null=True,blank=True)
  Name =models.CharField(primary_key=True,max_length=5)
  Hostname =models.CharField(max_length=60,null=True,blank=True)
  IP =models.CharField(max_length=20,null=True,blank=True)
  Windows_Server =models.CharField(max_length=50,null=True,blank=True)
  CPU =models.CharField(max_length=20,null=True,blank=True)
  Memory =models.CharField(max_length=20,null=True,blank=True)
  SQL_Version =models.CharField(max_length=50,null=True,blank=True)
  Disc_Size =models.CharField(max_length=20,null=True,blank=True)
  Location =models.CharField(max_length=20,null=True,blank=True)