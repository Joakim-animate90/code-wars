class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        
        self._set_order = []
    def _record(self, attr_name):
        if attr_name not in self._set_order:
            self._set_order.append(attr_name)
    
    def setAge(self, age):
        self.age = age
        self._record('age')
        return self
        
    def setSex(self, sex):
        self.sex = sex
        self._record('sex')
        return self
        
    def setName(self, name):
        self.name = name
        self._record('name')
        return self
        
    def hello(self):
        parts = ["Hello."]
        for attr in self._set_order:
            if attr == 'name' and self.name is not None:
                parts.append("My name is {}.".format(self.name))
            elif attr == 'age' and self.age is not None:
                parts.append(f"I am {self.age}.")
            elif attr == 'sex' and self.sex is not None:
                # map 'M' to male, anything else -> female (matches original)
                gender = "male" if self.sex == 'M' else "female"
                parts.append(f"I am {gender}.")
        return " ".join(parts)