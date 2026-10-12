# MP1 Data Pipeline

This  is a command-line data pipeline that loads a CSV file, validates it, cleans it, and saves the result. pipeline.py parses the command-line arguments, checks that the relevant files exist, and then runs each stage in order (load, validate, process, save). Settings such as required columns, numeric columns, and cleaning options live in config/config.yaml, so a different dataset only needs a config change, not a code change. src/data_loaders.py loads CSV, JSON, and YAML files, and src/data_validator.py checks required columns exist and removes invalid rows. src/data_processor.py removes duplicates, drops rows with missing values, removes outliers using IQR or z-score and builds a cleaning report comparing the data before and after. src/data_output.py saves the cleaned dataframe as a CSV file and creates the output folder if needed. src/utils.py holds the shared logging setup and input-file validation. The modules log problems and raise exceptions, and pipeline.py decides when the program should exit.

## Example

```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

```text
21:15:43 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, output=output/clean.csv, config=config/config.yaml
21:15:43 INFO     src.utils — Input file validated: fixtures/sample_data.csv
21:15:43 INFO     src.utils — Input file validated: config/config.yaml
21:15:43 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv (100 rows)
21:15:43 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
21:15:43 WARNING  src.data_validator — Invalid numeric value in rating at row 94: not_available
21:15:43 WARNING  src.data_validator — Invalid numeric value in rating at row 95: error
21:15:43 DEBUG    src.data_validator — Validation: 100 -> 98 rows (2 removed)
21:15:43 INFO     __main__ — Validation complete: 100 -> 98 rows
21:15:43 DEBUG    src.data_processor — remove_duplicates: 98 → 96 rows (2 removed)
21:15:43 DEBUG    src.data_processor — handle_missing: 96 → 94 rows
21:15:43 DEBUG    src.data_processor — rating: method=iqr, threshold=1.5, lower=43.625, upper=106.625, removed=2
21:15:43 INFO     __main__ — Processing complete: 98 -> 92 rows
21:15:43 DEBUG    src.data_output — Saved 92 rows to output/clean.csv
21:15:43 INFO     __main__ — Saved cleaned data to output/clean.csv

Cleaning report:
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```
