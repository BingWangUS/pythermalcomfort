"""In this example I am calculating the Standard Effective Temperature (SET) with the pythermalcomfort package"""

from pythermalcomfort.models import set_tmp

set_value = set_tmp(tdb=25, tr=25, v=.3, rh=60, met=1.2, clo=0.5)
print(f'set_value= {set_value}')

set_value = set_tmp(tdb=25, tr=25, v=.5, rh=60, met=1.2, clo=0.5)
print(f'set_value= {set_value}')

set_value = set_tmp(tdb=77, tr=77, v=.6, rh=60, met=1.2, clo=0.5, units='IP')
print(f'set_value= {set_value}')
