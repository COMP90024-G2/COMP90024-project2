import json
from shapely.geometry import Point
from shapely.geometry import MultiPolygon
from shapely.geometry.polygon import Polygon

GEO_LIST = []
postcode_file = 'postcode_mel.json'

with open(postcode_file,'r') as f:
    geo = json.load(f)
    for i in range(len(geo['features'])):
        geo_dict = {}
        geo_dict['location_id'] = geo['features'][i]['properties']['postcode']
        geo_dict['type'] = geo['features'][i]['geometry']['type']
        geo_dict['coordinates_polygon'] = geo['features'][i]['geometry']['coordinates']
        GEO_LIST.append(geo_dict)


def postcode(tweet_coor):
    if tweet_coor=='' or tweet_coor==None:
        return 'unknown'
    loc = Point([tweet_coor[1],tweet_coor[0]])
    for location in GEO_LIST:
        if location['type'] == 'Polygon':
            container_box = Polygon(location['coordinates_polygon'][0])
            if container_box.contains(loc):
                return(location['location_id'])
        elif location['type'] == 'MultiPolygon':
            for polygon in location['coordinates_polygon']:
                container_box = Polygon(polygon[0])
                if container_box.contains(loc):
                    return(location['location_id'])
    return 'not found'
                
