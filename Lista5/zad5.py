class FileLogger:
    def log(self, message):
        print(f"Logging to file: {message}")

class OrderProcessor:
    def __init__(self, logger: FileLogger = None):
        self.logger = logger if logger is not None else FileLogger()

    def process(self, order):
        self.logger.log(f"Processing order: {order}")
        return f"Order {order} processed"

processor = OrderProcessor()
print(processor.process("Order123"))