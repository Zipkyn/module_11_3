def introspection_info(obj):
    info = {
        "type": type(obj).__name__,
        "module": obj.__class__.__module__,
        "attributes": [],
        "methods": [],
    }

    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        if callable(attribute):
            info["methods"].append(attribute_name)
        else:  
            info["attributes"].append(attribute_name)

    return info

class SampleClass:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        return f"Value is {self.value}"

sample_obj = SampleClass(42)
info = introspection_info(sample_obj)
print(info)

