def detect_disaster(disaster_type, location):
    """
    Detect disaster information based on the disaster type and location (Offline Simulation).

    Parameters:
        disaster_type (str): Type of disaster (e.g., "earthquake", "flood", "glacier").
        location (str): Location to check for the disaster.

    Returns:
        str: Disaster information or a message indicating no disasters.
    """
    # Mock disaster data
    disaster_data = {
        "earthquake": [
            {"location": "California", "magnitude": 5.6, "details": "Moderate earthquake reported in California."},
            {"location": "Japan", "magnitude": 7.8, "details": "Severe earthquake in Japan, tsunami warning issued."}
        ],
        "flood": [
            {"location": "Mumbai", "severity": "High", "details": "Severe flood due to heavy rainfall in Mumbai."},
            {"location": "Bangladesh", "severity": "Medium", "details": "Flooding reported in low-lying areas of Bangladesh."}
        ],
        "glacier": [
            {"location": "Alaska", "movement": "Rapid", "details": "Rapid glacier movement detected in Alaska."},
            {"location": "Antarctica", "movement": "Stable", "details": "Glaciers in Antarctica are stable currently."}
        ]
    }

    # Check if disaster type is valid
    if disaster_type not in disaster_data:
        return "Invalid disaster type. Choose from: earthquake, flood, glacier."

    # Search for the disaster in the given location
    for disaster in disaster_data[disaster_type]:
        if disaster["location"].lower() == location.lower():
            return disaster["details"]

    return f"No {disaster_type} reported in {location}."

# Example usage
if __name__ == "__main__":
    print("Disaster Detection Application (Offline Simulation)")
    disaster_type = input("Enter disaster type (earthquake, flood, glacier): ").lower()
    location = input("Enter location: ")
    result = detect_disaster(disaster_type, location)
    print(result)
