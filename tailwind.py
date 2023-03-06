class TailwindCSS:
    def __init__(self, properties=None):
        self.properties = properties or {}

    def add_property(self, name, value):
        self.properties[name] = value

    def add_class(self, class_name):
        if 'class' not in self.properties:
            self.properties['class'] = ''
        self.properties['class'] += f' {class_name}'

    def remove_property(self, name):
        if name in self.properties:
            del self.properties[name]

    def remove_class(self, class_name):
        if 'class' in self.properties:
            classes = self.properties['class'].split()
            updated_classes = [c for c in classes if c != class_name]
            self.properties['class'] = ' '.join(updated_classes)

    def to_string(self):
        prop_strings = []
        for name, value in self.properties.items():
            if name == 'class':
                prop_strings.append(f'{name}="{value.strip()}"')
            else:
                prop_strings.append(f'{name}={value}')
        return ' '.join(prop_strings)



css = TailwindCSS()
css.add_class('bg-red-500')
css.add_class('text-white')
css.add_property('href', '"#"')
css.add_property('target', '_blank')
print(css.to_string())  # output: class="bg-red-500 text-white" href="#" target=_blank
css.remove_class('bg-red-500')
print(css.to_string())  # output: class="text-white" href="#" target=_blank
