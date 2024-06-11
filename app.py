from flask import Flask, request, jsonify

app = Flask(__name__)


website_visits = {}  # { websiteId: { customerId: {deviceId1, deviceId2, ... } } }
customer_visits = {}  # { (customerId, websiteId): set([deviceId1, deviceId2, ...]) }

@app.route('/')
def index():
    return "Website Hit Counter System is running!"

@app.route('/visit', methods=['POST'])
def visit_website():
    data = request.json
    customer_id = data['customerId']
    device_id = data['deviceId']
    website_id = data['websiteId']
    
    if website_id not in website_visits:
        website_visits[website_id] = {}
    if customer_id not in website_visits[website_id]:
        website_visits[website_id][customer_id] = set()
    
    website_visits[website_id][customer_id].add(device_id)
    
    if (customer_id, website_id) not in customer_visits:
        customer_visits[(customer_id, website_id)] = set()
    
    customer_visits[(customer_id, website_id)].add(device_id)
    
    return jsonify({"message": "Visit recorded"}), 200

@app.route('/customer_visit_count', methods=['GET'])
def get_website_visit_count_for_customer():
    customer_id = request.args.get('customerId')
    website_id = request.args.get('websiteId')
    
    if (customer_id, website_id) in customer_visits:
        count = len(customer_visits[(customer_id, website_id)])
        return jsonify({"customerId": customer_id, "websiteId": website_id, "visitCount": count}), 200
    else:
        return jsonify({"customerId": customer_id, "websiteId": website_id, "visitCount": 0}), 200

@app.route('/overall_hit_count', methods=['GET'])
def get_overall_website_hit_count():
    website_id = request.args.get('websiteId')
    
    if website_id in website_visits:
        count = sum(len(devices) for devices in website_visits[website_id].values())
        return jsonify({"websiteId": website_id, "hitCount": count}), 200
    else:
        return jsonify({"websiteId": website_id, "hitCount": 0}), 200

if __name__ == '__main__':
    app.run(debug=True)
