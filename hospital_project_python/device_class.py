# device class 
class Device:
    
    """Class representing a medical device in the hospital."""
    
    def __init__(self, name, device_type, status):
        """Initialize a device with its name, type, and status."""
        self.name = name  # The name of the device 
        self.device_type = device_type  # The type/category of the device 
        self.status = status  # Status of the device (e.g., "Operational", "Under Maintenance")

    def view_info(self):
        """Return basic information about the device."""
        return f"Device Name: {self.name}, Type: {self.device_type}, Status: {self.status}"

    def update_status(self, new_status):
        """Update the status of the device."""
        self.status = new_status