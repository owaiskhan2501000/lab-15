class ParentA:
    def method(self):
        return "ParentA method"

class ParentB:
    def method(self):
        return "ParentB method"

class Child(ParentA, ParentB):
    pass

# Example usage:
child_instance = Child()

print(child_instance.method())
# Output: ParentA method (Method resolution order follows the order of inheritance)
