import pandas as pd


def parse_file(path: str):
    data = pd.read_excel(
        path,
        header=[0, 2],
        engine='openpyxl'
    )
    data.columns = ['_'.join(col).strip()
                    for col in data.columns]
    return data
