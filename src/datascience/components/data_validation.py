import os
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema


            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    if col == all_cols[0]:
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Column '{col}' is not in the expected schema. Validation failed.\n")
                    else:
                        with open(self.config.STATUS_FILE, 'a') as f:
                            f.write(f"Column '{col}' is not in the expected schema. Validation failed.\n")
                else:
                    # Check data type
                    expected_dtype = all_schema[col]
                    actual_dtype = str(data[col].dtypes)

                    if actual_dtype != expected_dtype:
                        validation_status = False
                        if col == all_cols[0]:
                            with open(self.config.STATUS_FILE, 'w') as f:
                                f.write(f"Column '{col}' data type mismatch. Expected: {expected_dtype}, Found: {actual_dtype}.\n")
                        else:
                            with open(self.config.STATUS_FILE, 'a') as f:
                                f.write(f"Column '{col}' data type mismatch. Expected: {expected_dtype}, Found: {actual_dtype}.\n")
                    else:
                        if col == all_cols[0]:
                            with open(self.config.STATUS_FILE, 'w') as f:
                                f.write(f"Column '{col}' validated successfully.\n")
                        else:
                            with open(self.config.STATUS_FILE, 'a') as f:
                                f.write(f"Column '{col}' validated successfully.\n")

            return validation_status

        except Exception as e:
            raise e

