class TagContainer:
    def __init__(self, tags: object = None) -> object:
        if tags is None:
            self.tags = {}
        else:
            self.tags = tags

    def add(self, tag: str):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def get_tag(self, tag):
        return self.tags.get(tag.lower(), 0)

    def set_tag(self, tag: str, value: str):
        self.tags[tag.lower()] = value


cloud = TagContainer()
cloud.add("Python")
cloud.add("JS")

for tag_, count in cloud.tags.items():
    print(tag_, count)
