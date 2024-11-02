# Department class
class Department:
    
    def __init__(self, name, head):
        self.name = name  # Name of the department
        self.head = head  # The head of the department 
    
    def view_info(self):
        """View information about the department."""
        return f"Department: {self.name}, Head: {self.head}"