from ninja import Schema

class DesireSchema(Schema):
    name: str
    value: str
    description: str = None