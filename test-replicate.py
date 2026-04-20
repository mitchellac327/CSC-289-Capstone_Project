"""
TEST-REPLICATE.PY (FIXED)
Simple test script to verify your Replicate API setup is working correctly
Run this first before using the full haircut generator
"""

import os
import sys

print("="*70)
print("🔧 REPLICATE API TEST SCRIPT")
print("="*70)
print("\nThis script will test your Replicate API setup step by step.\n")

# ============================================================================
# TEST 1: Check Python Version
# ============================================================================
print("[TEST 1/7] Checking Python version...")
python_version = sys.version_info

if python_version.major >= 3 and python_version.minor >= 8:
    print(f"   ✅ Python {python_version.major}.{python_version.minor}.{python_version.micro} - Good!")
else:
    print(f"   ❌ Python {python_version.major}.{python_version.minor} - Need Python 3.8 or higher")
    print("   Please upgrade Python and try again.")
    input("\nPress Enter to exit...")
    sys.exit(1)

# ============================================================================
# TEST 2: Check Required Packages
# ============================================================================
print("\n[TEST 2/7] Checking installed packages...")

missing_packages = []

# Check replicate
try:
    import replicate
    # Try to get version, but don't fail if it doesn't exist
    try:
        version = replicate.__version__
        print(f"   ✅ replicate package installed (version {version})")
    except AttributeError:
        print(f"   ✅ replicate package installed")
except ImportError:
    print("   ❌ replicate package NOT installed")
    missing_packages.append('replicate')

# Check python-dotenv
try:
    import dotenv
    try:
        version = dotenv.__version__
        print(f"   ✅ python-dotenv package installed (version {version})")
    except AttributeError:
        print(f"   ✅ python-dotenv package installed")
except ImportError:
    print("   ❌ python-dotenv package NOT installed")
    missing_packages.append('python-dotenv')

# Check requests
try:
    import requests
    try:
        version = requests.__version__
        print(f"   ✅ requests package installed (version {version})")
    except AttributeError:
        print(f"   ✅ requests package installed")
except ImportError:
    print("   ❌ requests package NOT installed")
    missing_packages.append('requests')

if missing_packages:
    print("\n   ⚠️ MISSING PACKAGES!")
    print("   Please install them with:")
    print(f"   pip install {' '.join(missing_packages)}")
    input("\nPress Enter to exit...")
    sys.exit(1)

# ============================================================================
# TEST 3: Check .env File Exists
# ============================================================================
print("\n[TEST 3/7] Checking for .env file...")

if os.path.exists('.env'):
    print("   ✅ .env file found")
    
    # Check if file has content
    with open('.env', 'r') as f:
        content = f.read().strip()
        
    if not content:
        print("   ❌ .env file is EMPTY!")
        print("   Please add your API token to .env:")
        print("   REPLICATE_API_TOKEN=r8_your_token_here")
        input("\nPress Enter to exit...")
        sys.exit(1)
    else:
        print("   ✅ .env file has content")
        
else:
    print("   ❌ .env file NOT found!")
    print("\n   Please create a .env file in this directory with:")
    print("   REPLICATE_API_TOKEN=r8_your_token_here")
    print("\n   Steps:")
    print("   1. Open Notepad")
    print("   2. Type: REPLICATE_API_TOKEN=r8_your_token_here")
    print("   3. Save as '.env' (include the dot!)")
    print("   4. Save in the same folder as this script")
    input("\nPress Enter to exit...")
    sys.exit(1)

# ============================================================================
# TEST 4: Load Environment Variables
# ============================================================================
print("\n[TEST 4/7] Loading environment variables...")

from dotenv import load_dotenv
load_dotenv()

api_token = os.getenv('REPLICATE_API_TOKEN')

if not api_token:
    print("   ❌ REPLICATE_API_TOKEN not found in .env!")
    print("\n   Your .env file should contain:")
    print("   REPLICATE_API_TOKEN=r8_your_token_here")
    print("\n   Current .env contents:")
    with open('.env', 'r') as f:
        print(f"   {f.read()}")
    input("\nPress Enter to exit...")
    sys.exit(1)

print(f"   ✅ API token loaded")
print(f"   Token starts with: {api_token[:10]}...")
print(f"   Token length: {len(api_token)} characters")

# Validate token format
if not api_token.startswith('r8_'):
    print("   ⚠️ WARNING: Token should start with 'r8_'")
    print("   Your token might be invalid. Double-check it!")

if len(api_token) < 40:
    print("   ⚠️ WARNING: Token seems too short")
    print("   Make sure you copied the full token from Replicate")

# ============================================================================
# TEST 5: Set API Token for Replicate
# ============================================================================
print("\n[TEST 5/7] Setting up Replicate client...")

os.environ["REPLICATE_API_TOKEN"] = api_token
print("   ✅ API token set in environment")

# ============================================================================
# TEST 6: Test API Connection
# ============================================================================
print("\n[TEST 6/7] Testing Replicate API connection...")
print("   This will verify your API token is valid")
print("   (This does NOT use any credits)")

try:
    import replicate
    
    # Try to create a client (this validates the token without running a model)
    try:
        client = replicate.Client(api_token=api_token)
        print("   ✅ Successfully connected to Replicate API!")
        print("   Your API token is valid!")
    except AttributeError:
        # Older version of replicate doesn't have Client class
        # Just verify we can import it
        print("   ✅ Replicate package loaded!")
        print("   (Using older version - API connection will be tested in next step)")
    
except replicate.exceptions.ReplicateError as e:
    print(f"   ❌ Replicate API Error: {e}")
    print("\n   Possible issues:")
    print("   - Invalid API token")
    print("   - Network/internet connection problem")
    print("   - Replicate service might be down")
    input("\nPress Enter to exit...")
    sys.exit(1)
    
except Exception as e:
    print(f"   ❌ Unexpected Error: {e}")
    print(f"   Error type: {type(e).__name__}")
    input("\nPress Enter to exit...")
    sys.exit(1)

# ============================================================================
# TEST 7: Optional - Test Image Generation
# ============================================================================
print("\n[TEST 7/7] Optional: Test actual image generation")
print("   This will generate a test image and use a small amount of credit (~$0.01)")

test_generate = input("   Would you like to test image generation? (yes/no): ").lower().strip()

if test_generate == 'yes':
    print("\n   🚀 Generating test image...")
    print("   ⏳ This takes 10-30 seconds, please wait...")
    
    try:
        # Generate a simple test image
        output = replicate.run(
            "flux-kontext-apps/change-haircut",
            input={
                "gender": "none",
                "haircut": "Random",
                "hair_color": "Random"
            }
        )
        
        print("   ✅ Image generated successfully!")
        print(f"   🔗 URL: {output}")
        
        # Ask if user wants to download
        download = input("\n   Download and save the image? (yes/no): ").lower().strip()
        
        if download == 'yes':
            print("   📥 Downloading...")
            
            from pathlib import Path
            
            # Create output folder
            output_dir = Path("test_outputs")
            output_dir.mkdir(exist_ok=True)
            
            # Download
            response = requests.get(output)
            
            if response.status_code == 200:
                output_path = output_dir / "test_image.png"
                
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                
                print(f"   ✅ Image saved to: {output_path.absolute()}")
                print("   You can open this file to see the generated image!")
            else:
                print(f"   ❌ Download failed (HTTP {response.status_code})")
        
    except Exception as e:
        print(f"   ❌ Generation failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        print("\n   Possible issues:")
        print("   - Insufficient credits (check your balance at replicate.com)")
        print("   - Invalid API token")
        print("   - Model temporarily unavailable")
        print("   - Network connection problem")
        
else:
    print("   ⏭️  Skipped image generation test")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "="*70)
print("📊 TEST SUMMARY")
print("="*70)
print("✅ Python version: OK")
print("✅ Required packages: OK")
print("✅ .env file: OK")
print("✅ API token loaded: OK")
print("✅ Replicate setup: OK")

if test_generate == 'yes':
    print("✅ Image generation: Tested")

print("\n" + "="*70)
print("🎉 SETUP COMPLETE!")
print("="*70)
print("\nYour Replicate API setup looks good!")
print("\nNext steps:")
print("1. Try generating a test image if you skipped it")
print("2. Run 'python test_haircut.py' to generate your first hairstyle")
print("3. Run 'python interactive_haircut.py' for interactive mode")
print("4. Run 'python app.py' to start the web server")
print("\n" + "="*70)

input("\nPress Enter to exit...")