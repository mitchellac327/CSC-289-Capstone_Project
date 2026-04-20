README - HAIRCUT AI GENERATOR
Backend Python Script for Swift Integration

===============================================================================
OVERVIEW
===============================================================================

This Python script generates AI hairstyle previews using Replicate's API.
It's designed to be used as a backend service for a Swift iOS app.

The Python script can run as:
1. A Flask REST API (recommended for production)
2. A standalone GUI (for testing/development)

===============================================================================
WHAT YOU NEED
===============================================================================

1. Python 3.8 or higher
2. Replicate API account (https://replicate.com)
3. API token from Replicate ($5 free credit)
4. Required Python packages (see below)

===============================================================================
QUICK SETUP
===============================================================================

1. Install Python packages:
   pip install replicate requests flask flask-cors

2. Create a .env file in the project folder with your API token:
   REPLICATE_API_TOKEN=r8_your_token_here

3. Test the script works:
   python FIXED_image_upload.py

===============================================================================
FILES IN THIS PROJECT
===============================================================================

FIXED_image_upload.py - GUI version (for testing)
api_server.py - Flask REST API (for Swift integration)
.env - Your API token (KEEP SECRET - don't commit to git!)

===============================================================================
FOR SWIFT INTEGRATION - USE THE REST API
===============================================================================

STEP 1: Start the Python Flask server

   python api_server.py

   Server runs at: http://localhost:5000

STEP 2: In Swift, make HTTP requests to these endpoints:

   POST /api/generate
   - Upload image as multipart/form-data
   - Parameters: hairstyle, hair_color, gender, user_tier
   - Returns: JSON with image_id and image_url

   GET /api/image/{image_id}
   - Downloads the generated image

   GET /api/options
   - Gets available hairstyles and colors

   GET /health
   - Checks if server is running

===============================================================================
API EXAMPLE - HOW SWIFT CALLS PYTHON
===============================================================================

// Swift code to call the Python API:

let url = URL(string: "http://localhost:5000/api/generate")!
var request = URLRequest(url: url)
request.httpMethod = "POST"

let boundary = UUID().uuidString
request.setValue("multipart/form-data; boundary=\(boundary)", 
                forHTTPHeaderField: "Content-Type")

// Build multipart form data with:
// - image file (JPEG/PNG)
// - hairstyle (e.g., "Short", "Fade")
// - hair_color (e.g., "Black", "Brown")
// - gender ("none", "male", "female")
// - user_tier ("pro" or "free")

// Send request and get JSON response:
// {
//   "success": true,
//   "image_id": "abc123",
//   "image_url": "/api/image/abc123"
// }

// Then download image from: http://localhost:5000/api/image/abc123

===============================================================================
DEPLOYMENT
===============================================================================

For production, deploy the Flask API to:
- Heroku
- Railway
- Google Cloud Run
- AWS EC2
- Any server that runs Python

Then update Swift to use your production URL:
https://your-app.herokuapp.com instead of http://localhost:5000

===============================================================================
HOW IT WORKS
===============================================================================

1. Swift app sends photo + style preferences to Python Flask API
2. Python receives image and parameters
3. Python calls Replicate AI API to generate new hairstyle
4. Replicate returns generated image URL
5. Python downloads and saves the image
6. Python returns image_id to Swift
7. Swift downloads the final image from Python server

===============================================================================
COSTS
===============================================================================

Each AI generation costs approximately $0.01 - $0.05
You get $5 free credit when signing up ($100-500 images)

Gate this feature to "Pro" users only to control costs.

===============================================================================
IMPORTANT SECURITY NOTES
===============================================================================

1. NEVER put the API token in your Swift app
   - API keys MUST stay on the server
   - Users could extract it from the app

2. Keep .env file secret
   - Add .env to .gitignore
   - Never commit to GitHub

3. Validate user tier on server
   - Check if user is "Pro" before generating
   - Don't trust the Swift app to do this check

===============================================================================
TESTING THE API
===============================================================================

Test with curl:

# Health check
curl http://localhost:5000/health

# Get options
curl http://localhost:5000/api/options

# Generate (requires image file)
curl -X POST http://localhost:5000/api/generate \
  -F "image=@photo.jpg" \
  -F "hairstyle=Short" \
  -F "hair_color=Black" \
  -F "gender=none" \
  -F "user_tier=pro"

===============================================================================
TROUBLESHOOTING
===============================================================================

Problem: "Module not found"
Solution: pip install replicate requests flask flask-cors

Problem: "API token not found"
Solution: Create .env file with REPLICATE_API_TOKEN=your_token

Problem: "Connection refused"
Solution: Make sure Flask server is running (python api_server.py)

Problem: "Generation failed"
Solution: Check you have API credits at https://replicate.com/account

===============================================================================
ARCHITECTURE DIAGRAM
===============================================================================

Swift iOS App  →  HTTP POST  →  Python Flask API  →  Replicate AI
    (UI)                         (Image Processing)    (AI Generation)
                ←  JSON/Image ←

===============================================================================
ENDPOINTS REFERENCE
===============================================================================

POST /api/generate
    Input: multipart/form-data
        - image: file (required)
        - hairstyle: string (e.g., "Short", "Fade")
        - hair_color: string (e.g., "Black", "Brown")
        - gender: string ("none", "male", "female")
        - user_tier: string ("pro", "free")
    
    Output: JSON
        {
            "success": true/false,
            "image_id": "abc123",
            "image_url": "/api/image/abc123",
            "error": "error message if failed"
        }

GET /api/image/{image_id}
    Output: PNG/JPG image file

GET /api/options
    Output: JSON
        {
            "success": true,
            "hairstyles": ["Short", "Fade", "Bob", ...],
            "colors": ["Black", "Brown", "Blonde", ...],
            "genders": ["none", "male", "female"]
        }

GET /health
    Output: JSON
        {
            "status": "ok",
            "message": "Haircut AI API is running"
        }

===============================================================================
DEVELOPMENT WORKFLOW
===============================================================================

1. Run Python server locally: python api_server.py
2. Swift app connects to: http://localhost:5000
3. Make sure iPhone/simulator and Mac are on same WiFi
4. Get your Mac's IP address: ipconfig getifaddr en0 (Mac)
5. Swift connects to: http://192.168.1.X:5000

===============================================================================
CONTACT INFO
===============================================================================

If you have questions about the Python backend:
- Check the code comments in api_server.py
- All functions are documented with examples
- Print statements show what's happening

For Replicate API issues:
- Documentation: https://replicate.com/docs
- Status: https://status.replicate.com

===============================================================================
THAT'S IT!
===============================================================================

You now have everything you need to integrate this Python backend
with your Swift app. The API is simple REST - just HTTP requests.

Good luck with the app!
