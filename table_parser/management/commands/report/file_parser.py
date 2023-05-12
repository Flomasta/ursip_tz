import pandas as pd


def parse_file(path: str):
    data = pd.read_excel(
        path,
        header=[0, 2],
        engine='openpyxl'
    )
    # data.columns = ['_'.join(col).strip()
    #                 for col in data.columns]
    # Я бы написал более generic-код для того, тчобы загрузить файл,
    # но, как мне кажется, код этого отчёта довольно индивидуален и,
    # конкретно в данном случае, будет лучше и понятнее захардкодить колонки.

    data.columns = [
        'id',
        'company',
        'fact_qliq_data1',
        'fact_qliq_data2',
        'fact_qoil_data1',
        'fact_qoil_data2',
        'forecast_qliq_data1',
        'forecast_qliq_data2',
        'forecast_qoil_data1',
        'forecast_qoil_data2'
    ]
    data = data.drop(columns=['id'])
    return data
