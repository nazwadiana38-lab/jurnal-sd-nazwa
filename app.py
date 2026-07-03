from http.server import BaseHTTPRequestHandler, HTTPServer

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Tampilan yang akan muncul di browser kamu nanti
        self.wfile.write(b"<h1>Halo Guest! Aplikasi ini berjalan di dalam kontainer Docker.</h1>")
        self.wfile.write(b"<p>Status Lingkungan: production</p>")
        self.wfile.write(b"<h2>Versi 2.0 - Stabil</h2>")

if __name__ == "__main__":
    web_server = HTTPServer(("0.0.0.0", 5000), MyServer)
    print("Server berhasil berjalan di port 5000...")
    web_server.serve_forever()
