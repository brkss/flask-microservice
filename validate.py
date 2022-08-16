from cerberus import Validator

add_book_schema = {'name': {"type": "string", 'required': True}, 'author': {"type": "string", "required": True}, "price": {"type": "integer", "required": True}}

def validate_adding_book_data(document):
    v = Validator(add_book_schema)
    v.allow_unknown = True
    return v.validate(document)
