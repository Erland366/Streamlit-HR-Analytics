
def write_to_data(text):
    with open("data.csv", "a") as f:
        f.write(f"{text}\n")

def create_info(data, dtype_column="dtype", count_column="count"):
    import pandas as pd
    pd.concat([pd.DataFrame(data.dtypes), data.count()], axis=1).set_axis([dtype_column, count_column], axis="columns")

def test():
    print("Hello world")
