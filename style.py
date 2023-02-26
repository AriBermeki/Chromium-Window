class CSS:
    def __init__(self):
        self.rules = []

    def add_rule(self, selector, styles):
        rule = CSSRule(selector, styles)
        self.rules.append(rule)

    def __str__(self):
        return "\n".join([str(rule) for rule in self.rules])


class CSSRule:
    def __init__(self, selector, styles):
        self.selector = selector
        self.styles = styles

    def __str__(self):
        styles_str = "; ".join([f'{prop}: {val}' for prop, val in self.styles.items()])
        return f'{self.selector} {{ {styles_str} }}'