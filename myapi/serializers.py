from rest_framework import serializers
from .models import Vouchers

class VouchersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vouchers
        fields = (
        'id',
        'kode_voucher',
        'kota',
        'diskon',
        'nama_merch',
        'nama_menu',
        'tgl_mulai',
        'tgl_selesai',
        'alamat',
        'info',
        )
