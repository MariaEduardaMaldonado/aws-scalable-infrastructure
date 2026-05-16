from flask import Flask, url_for
import os
import socket
import requests

app = Flask(__name__)

def get_instance_id():
    """Gets the Instance ID of the current EC2 instance from the AWS metadata service."""
    try:
        response = requests.get("http://169.254.169.254/latest/meta-data/instance-id", timeout=2)
        return response.text
    except requests.RequestException:
        return "Unavailable"

def get_instance_az():
    """Gets the availability zone of the current EC2 instance through the AWS metadata service."""
    try:
        response = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone", timeout=2)
        return response.text
    except requests.RequestException:
        return "Unavailable"
    
def get_instance_ip():
    """Gets the IP of the current EC2 instance through the AWS metadata service."""
    try:
        response = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4')
        return response.text
    except requests.RequestException:
        return "Unavailable"

@app.route('/')
def show_instance_info():
    ip_address = get_instance_ip()
    instance_id = get_instance_id()
    availability_zone = get_instance_az()
    
    return f"""
    <html>
        <head>
            <title>EC2 Instance</title>
            <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
        </head>
        <body>
            <div class="container">
                <h1>Current Instance Information</h1>
                <h1>Flask Application</h1>
                <div class="info">Instance ID: <span>{instance_id}</span></div>
                <div class="info">Instance IP: <span>{ip_address}</span></div>
                <div class="info">Availability Zone: <span>{availability_zone}</span></div>
            </div>
            <div class="footer">
                <p>&copy; 2025 Load balancing - EC2</p>
            </div>
        </body>
    </html>
    """

@app.route('/health')
def health_check():
    """Endpoint de health check para Load Balancer."""
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
