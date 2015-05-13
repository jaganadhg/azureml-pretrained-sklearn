import pandas as pd

def azureml_main(data_frame):
        import bostonp
        price = bostonp.predict_hp(data_frame)
        data_frame["price"] = price
        return data_frame
