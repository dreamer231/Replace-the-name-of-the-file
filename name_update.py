def decorator_name(front,end):
    def wrap(func):
        def wrapped(*args, **kwargs):
            print(f"{front} {func.__name__} {end}")
            return func(*args, **kwargs)
        return wrapped
    return wrap

def update_file_name(name):
    @decorator_name("Updating", "completed")
    def rename():
        print(f"File renamed to {name}")
    rename()

if __name__ == "__main__":
    update_file_name("new_file.txt")