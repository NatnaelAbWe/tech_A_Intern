from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

def get_user_location():
    """
    Retrieves GPS coordinates (latitude & longitude) based on user input (city, country, etc.).
    Uses the Nominatim geocoder for location lookup.
    """
    geolocator = Nominatim(user_agent="location_finder")
    
    while True:
        user_input = input("🌍 Enter your location (e.g., city, country): ").strip()
        
        if not user_input:
            print("⚠️ Location input cannot be empty. Please try again.")
            continue

        try:
            user_location = geolocator.geocode(user_input, timeout=10)
            
            if user_location:
                print("\n📍 Location Found!")
                print(f"🌎 Address: {user_location.address}")
                print(f"🗺 Latitude: {user_location.latitude}")
                print(f"🗺 Longitude: {user_location.longitude}")
                break
            else:
                print("❌ Location not found. Please try again with a more specific place.")
        
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"⏳ Geocoding service issue: {e}")
            print("🔄 Retrying...")

if __name__ == "__main__":
    get_user_location()
