from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Pega variáveis de ambiente
    app_name = os.getenv('APP_NAME', 'Default App')
    environment = os.getenv('ENVIRONMENT', 'development')
    version = os.getenv('VERSION', '1.0.0')
    
    return f'''
    <html>
        <head>
            <title>{app_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .env-info {{ background: #f0f0f0; padding: 20px; border-radius: 8px; margin: 20px 0; }}
                .env-var {{ margin: 10px 0; }}
            </style>
        </head>
        <body>
            <h1>🚀 {app_name}</h1>
            <p>Hello from TEE Cloud!</p>
            
            <div class="env-info">
                <h3>Environment Variables:</h3>
                <div class="env-var"><strong>APP_NAME:</strong> {app_name}</div>
                <div class="env-var"><strong>ENVIRONMENT:</strong> {environment}</div>
                <div class="env-var"><strong>VERSION:</strong> {version}</div>
                <div class="env-var"><strong>PORT:</strong> {os.getenv('PORT', '8080')}</div>
            </div>
            
            <p><em>Environment: {environment} | Version: {version}</em></p>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'environment': os.getenv('ENVIRONMENT', 'development')}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False) 