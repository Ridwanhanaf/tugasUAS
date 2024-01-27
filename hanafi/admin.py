
from django.contrib import admin 
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis,ChatID
 
class DataKategoriAdmin(admin.ModelAdmin): 
    list_display = ("nama","aktif","banner_satu","banner_dua",) 
    prepopulated_fields = {"slug": ("nama",)} 
 
class DataProdukAdmin(admin.ModelAdmin): 
    list_display = ("nama_produk", "gambar","harga","no_whatsapp",) 
    prepopulated_fields = {"slug": ("nama_produk",)} 
 
class DataKontak(admin.ModelAdmin): 
    list_display = ("nama", "no_whatsapp","subject","email","isi",) 
 
class DataProfil(admin.ModelAdmin): 
    list_display = ("nama", "keterangan","gambar",) 
 
 
admin.site.register(Produk,DataProdukAdmin) 
admin.site.register(Kategori,DataKategoriAdmin) 
# admin.site.register(Produk) 
admin.site.register(Slide) 
admin.site.register(Kontak,DataKontak) 
admin.site.register(Profil,DataProfil) 
admin.site.register(Statis)
admin.site.register(ChatID)