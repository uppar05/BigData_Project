#!/usr/bin/env python
import shapefile
import sys
import traceback
from datetime import datetime


class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Polygon:
	def __init__(self,points):
		self.points = points
		self.nvert = len(points)

		minx = maxx = points[0].x
		miny = maxy = points[0].y
		for i in xrange(1,self.nvert):
			minx = min(minx,points[i].x)
			miny = min(miny,points[i].y)
			maxx = max(maxx,points[i].x)
			maxy = max(maxy,points[i].y)

		self.bound = (minx,miny,maxx,maxy)


	def contains(self,pt):
		firstX = self.points[0].x
		firstY = self.points[0].y
		testx = pt.x
		testy = pt.y
		c = False
		j = 0
		i = 1
		nvert = self.nvert
		while (i < nvert) :
			vi = self.points[i]
			vj = self.points[j]
			
			if(((vi.y > testy) != (vj.y > testy)) and (testx < (vj.x - vi.x) * (testy - vi.y) / (vj.y - vi.y) + vi.x)):
				c = not(c)

			if(vi.x == firstX and vi.y == firstY):
				i = i + 1
				if (i < nvert):
					vi = self.points[i];
					firstX = vi.x;
					firstY = vi.y;
			j = i
			i = i + 1
		return c

	def bounds(self):
		return self.bound


names = []
Polygons = []
    
def find_boroughs(boxes, points, lon, lat):
    idxs = []
    for idx,box in enumerate(boxes):
        if box[0] <= lon and box[2] >= lon and box[1] <= lat and box[3] >= lat:
            idxs.append(idx)
            #print names[idx]
    if len(idxs) == 0:
        return [-1]

    newidx = []
    if len(idxs) > 1:
        pt = Point(lon, lat)
        for idx in idxs:
            if Polygons[idx].contains(pt):
                newidx.append(idx)
        if len(newidx) > 0:
            return newidx
        else:
            return idxs
    else:
        return idxs

    
    
def main(argv):
#    if len(argv) < 1:
#        print("input filename")
#        return

    sf = shapefile.Reader('../../data/ZillowNeighborhoods-NY')

    records = sf.records()
    shapes = sf.shapes()

    # Filter out only those of New York City
    idx = 0
    boxes = []
    points = []

    for index, record in enumerate(records):
        boroughs = ['New York', 'Bronx', 'Queens', 'Kings', 'Richmond']
        if record[1] in boroughs:
            '''
            join_data = {
                '_id_': idx,
                'name': record,
                'gps': shapes[index].points #shapes[index].bbox
            }
            '''
            boxes.append(shapes[index].bbox)
            points.append(shapes[index].bbox)
            names.append(record)
    #        print join_data
            idx += 1
            pps = []
            for cp in shapes[index].points:
                #print cp
                pps.append(Point(cp[0], cp[1]))
            Polygons.append(Polygon(pps))
    
#    f = open(argv[0], 'r')
#    for line in f.readlines():
    for line in sys.stdin:
        try:
            keys = []
            values = []
            rowtype = 1
            items = line.strip().split(',')
    
            if len(items) > 0:
                if items[0] == "VendorID":
                    continue
            date_obj = datetime.strptime(items[1], '%Y-%m-%d %H:%M:%S')
            keys.append(str(date_obj.year))
            keys.append(str(date_obj.month))
            keys.append(str(date_obj.day))
            date_end = datetime.strptime(items[2], '%Y-%m-%d %H:%M:%S')
            rate_ID = 0
        
            values.append(items[0])
            td = date_end - date_obj
            total_second = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
            values.append(str(total_second/60.0))
            if len(items) == 23 or len(items) == 21: #green #21 for after 7
                rate_ID = int(items[4])
                rowtype = 1
                plon = float(items[5])
                plat = float(items[6])
                dlon = float(items[7])
                dlat = float(items[8])
            elif len(items) == 19: #yellow
                rate_ID = int(items[7])
                rowtype = 2
                plon = float(items[5])
                plat = float(items[6])
                dlon = float(items[9])
                dlat = float(items[10])
            
            pboro = find_boroughs(boxes, points, plon, plat)
            dboro = find_boroughs(boxes, points, dlon, dlat)
#            print "%s\t%d,%d,%s,%s" % (",".join(keys), rowtype, rate_ID, "_".join(map(str,pboro)), "_".join(map(str,dboro)))
#            print "%s\t%s,%s" % (",".join(keys), "_".join(map(str,pboro)), "_".join(map(str,dboro)))
            print "%s,%s\t1" % (",".join(keys), min(pboro))
        except:
            traceback.print_exc()
        
if __name__ == "__main__":
    main(sys.argv[1:])
