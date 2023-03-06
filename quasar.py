class QuasarComponent:
    def __init__(self, tag=None, classes=None, props=None):
        self.tag = tag
        self.classes = classes or []
        self.props = props or {}

    def add_class(self, class_name):
        self.classes.append(class_name)

    def remove_class(self, class_name):
        if class_name in self.classes:
            self.classes.remove(class_name)

    def add_prop(self, prop_name, prop_value):
        self.props[prop_name] = prop_value

    def remove_prop(self, prop_name):
        if prop_name in self.props:
            del self.props[prop_name]

    def quasar_data(self):
        class_str = " ".join(self.classes)
        prop_str = " ".join([f'{prop}="{value}"' for prop, value in self.props.items()])
        return f'class="{class_str}" {prop_str}>'

    def to_html(self):
        class_str = " ".join(self.classes)
        prop_str = " ".join([f'{prop}="{value}"' for prop, value in self.props.items()])
        return f'<{self.tag} class="{class_str}" {prop_str}></{self.tag}>'




button = QuasarComponent(classes=['btn', 'btn-primary'], props={'type': 'button', 'disabled': True})
print(button.quasar_data())
