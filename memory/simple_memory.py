class MemoryDB:
    def __init__(self):
        self.store_data = []

    def store(self, input_text, output_text):
        self.store_data.append((input_text, output_text))

    def query(self, query_text):
        for input_text, output_text in reversed(self.store_data):
            if query_text.lower() in input_text.lower():
                return output_text
        return ""