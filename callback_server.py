import http.server
import socketserver
import json
PORT = 8081

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Process the callback data here
        try:
            callback_data = json.loads(post_data)
        except json.JSONDecodeError as e:
            callback_data = {
                "error": "Invalid JSON format",
                "details": str(e)
            }
        
        # Print the received request data
        print("Received POST request data:")
        print(callback_data)
        
        # Send a JSON response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        response_data = {
            "message": "Callback data received successfully",
            "status": "ok"
        }
        self.wfile.write(json.dumps(response_data).encode())

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
