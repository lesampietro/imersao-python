class Operation:
    cents: int
    operation_type: str #operation nature
    decription: str #operation type

    def __init__(self, cents: int, description: str):
    """Inits an object of type Operation"""
    self.cents = cents
    self.description = description

    def init_operation_type(cents: int) -> None:
        