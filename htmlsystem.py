class HTMLTag:
    def __init__(self, tag_name, attributes=None, content=None, style=None):
        self.tag_name = tag_name
        self.attributes = attributes or {}
        self.content = content or []
        self.style = style or {}

    def __str__(self):
        attrs_str = " ".join([f'{attr}="{val}"' for attr, val in self.attributes.items()])
        style_str = "; ".join([f'{prop}: {val}' for prop, val in self.style.items()])
        if style_str:
            style_str = f' style="{style_str}"'
        content_str = "".join([str(item) for item in self.content])
        return f'<{self.tag_name} {attrs_str}{style_str}>{content_str}</{self.tag_name}>'

    def add_content(self, content):
        self.content.append(content)

    def set_attribute(self, attr, val):
        self.attributes[attr] = val

    def set_style(self, prop, val):
        self.style[prop] = val


