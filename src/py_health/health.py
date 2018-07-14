from src.py_health import health_pb2

def print_bottle(note_string):
    my_bottle = health_pb2.Bottle(note='Ahoy!')
    return my_bottle.SerializeToString()
