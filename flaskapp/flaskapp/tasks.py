import csv
from datetime import datetime
from flaskapp import app,db
from models import Orders

def update_table():
	count = 1
	with open('files/orders.csv','r') as f:
	    reader = csv.DictReader(f.read().splitlines())
	    for row in reader:
	    	print "count : ", count
	    	order = Orders()
	    	order.order_status = row['order_status']
	    	order.order_id = row['order_id']
	    	order.product_name = row['product_name']
	    	order.product_url = row['product_url']
	    	try:
	    		order.cost_price = float(row['cost_price']) * 66
	    	except:
	    		order.cost_price = 0
	    	order.created_on = datetime.utcnow()
	    	db.session.add(order)
	    	db.session.commit()
	    	count+=1
	    	print len(Orders.query.all())
	    print count

update_table()