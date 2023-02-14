import pandas as pd
from kats.consts import TimeSeriesData
from kats.models.prophet import ProphetModel, ProphetParams

def forecast(file_name, time_col_name, steps):

    df = pd.read_csv(file_name, header=0, index_col=0)

    ts = TimeSeriesData(df=df, time_col_name=time_col_name)

    params = ProphetParams(seasonality_mode="multiplicative")

    m = ProphetModel(ts, params=params)

    m.fit()

    fcst = m.predict(steps=steps, freq="D")

    fcst = fcst.drop(columns=["fcst_lower", "fcst_upper"])

    fcst = fcst.rename(columns={"fcst": "prediction"})
    fcst = fcst.rename(columns={"time": time_col_name})

    data = fcst.to_dict(orient="records")

    for i in data:

        try:
            print(i)
            i["prediction"] = abs(i["prediction"])
            i[time_col_name] = str(i[time_col_name])[:10]

        except:

            pass

    return data