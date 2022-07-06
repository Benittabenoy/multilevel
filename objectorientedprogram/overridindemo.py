class Parent:
    def properties(self):
        self.props = {"mobile": "redmi", "bike": "duke"}
        return self.props


class Child(Parent):
    def properties(self):
        props = super().properties()
        props["car"] = "swift"
        return props
ch = Child()
print(ch.properties())