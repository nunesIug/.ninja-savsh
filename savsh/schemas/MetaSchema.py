from ninja import Schema

class MetaSchema(Schema):
    value: str
    description: str = None