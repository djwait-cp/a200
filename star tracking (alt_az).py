import numpy as np # install numpy
import math

# convert angular distances (h,m,s OR d,m,s) to hours or degrees
def toHours(anglist):
    return anglist[0] + anglist[1]/60.0 + anglist[2]/3600.0

# enter in target coordinates (RA/dec)

'''target = {
    'name':'Polaris',
    'RA_hms': [2, 57, 25.5],
    'dec_dms': [89, 21, 25.6]
}'''

'''target = {
    'name':'Betelgeuse',
    'RA_hms': [5, 56, 18.6],
    'dec_dms': [7, 24, 30.5]
}'''

'''target = {
    'name':'Alioth',
    'RA_hms': [12, 54, 58.0],
    'dec_dms': [55, 50, 33.9]
}'''

'''target = {
    'name':'Hamal',
    'RA_hms': [2, 8, 20.0],
    'dec_dms': [23, 33, 41.6]
}'''

target = {
    'name':'Alphard',
    'RA_hms': [9, 28, 38.0],
    'dec_dms': [-8, 45, 6.8]
}

target['RA_h'] = toHours(target['RA_hms'])
target['dec_d'] = toHours(target['dec_dms'])

# enter in observer coordinates and time (in Julian date, JD; assume conversion is done so D is given)
observer = {
    'latitude': 35.29067,
    'longitude': -120.65786,
    'time_hms': [20, 0, 0],
    'Julian Date': 7721.33333
}

observer['time_h'] = toHours(observer['time_hms'])

# Compute Greenwich mean sidereal time (in hours) at 0h
GMST = 18.697374558 + 24.06570982441908 * observer['Julian Date']

# local hour angle (radians)
LHA = math.radians( (GMST - target['RA_h']) * 15 + observer['longitude'] )

# φ = 90 - Lat (radians)
phi = math.radians(observer['latitude'])
delta = math.radians(target['dec_d'])

# gives altitude, (radians)
altitude = math.asin( math.sin(delta)*math.sin(phi) + math.cos(delta)*math.cos(phi)*math.cos(LHA))
# convert to degrees 
altitude_deg = math.degrees(altitude)

# gives azimuth, A 
# sin(A) = - sin(LHA)*cos(δ) / cos(a)
azimuth= math.asin( -math.sin(LHA)*math.cos(delta) / math.cos(altitude))
# convert to degrees
azimuth_deg = math.degrees(azimuth)

print('GMST = %f'%GMST)
print('LHA = %f'%LHA)
print('phi = %f'%phi)
print('delta = %f'%delta)
print('altitude in radians = %f'%altitude)
print('azimuth in radians = %f'%azimuth)
print('altitude in degrees = %f'%altitude_deg)
print('azimuth in degrees = %f'%azimuth_deg)
