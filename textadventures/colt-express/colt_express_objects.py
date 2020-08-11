#!/usr/bin/env python3

class Entity():

    def __init__(self, title, description):
        self.title = title
        self.description = description

class Item(Entity):

    def __init__(self, title, description, takeable=True):
        self.takeable = takeable
        super().__init__(title, description)
