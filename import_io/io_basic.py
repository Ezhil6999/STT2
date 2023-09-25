import io

with io.open('example.txt','r',encoding='utf-8') as file:
    content=file.read()
    print(content)

#-------------------------------------------------------------------

# Create a string buffer using StringIO
buffer = io.StringIO()
buffer.write("Hello, world!")
buffer.write(" hi how are you")
# Read from the buffer
data = buffer.getvalue()
print(data)

#-------------------------------------------------------------------

# Create a binary buffer using BytesIO
binary_buffer = io.BytesIO()
binary_buffer.write(b'\x01\x02\x03\x04')

# Read from the binary buffer
binary_data = binary_buffer.getvalue()
print(binary_data)


#----------------------------------------------------------------


class MyCustomIO(io.IOBase):
    def __init__(self):
        super().__init__()
        self.data = {}
if __name__ == "__main__":
    # Create an instance of MyCustomIO
    custom_io = MyCustomIO()

    # Write key-value pairs
    custom_io.write("name = John\nage = 30\ncity = New York")
    # print("hi",custom_io.read(),"hi")
    # Read and print the stored data
    stored_data = custom_io.read()
    print("Stored Data:")
    print(stored_data)

    # Add a new key-value pair
    custom_io.write("language = Python")

    # Read and print the updated data
    updated_data = custom_io.read()
    print("\nUpdated Data:")
    print(updated_data)
# Output:
                    # hi name = John
                    # age = 30
                    # city = New York hi
                    # Stored Data:
                    # name = John
                    # age = 30
                    # city = New York

                    # Updated Data:
                    # name = John
                    # age = 30
                    # city = New York
                    # language = Python