import pandas as pd



# - AUTO FIT COLUMN EXCEL FILE : START -------------------------------------------------------------------
# *Note: install 'pip install xlsxwriter' before use
def autosize_excel_columns_df(worksheet, df, offset=0):
  for idx, col in enumerate(df):
    series = df[col]
    max_len = max((
      series.astype(str).map(len).max(),
      len(str(series.name))
    )) + 1
    worksheet.set_column(idx + offset, idx + offset, max_len)


def autosize_excel_columns(worksheet, df):
  autosize_excel_columns_df(worksheet, df.index.to_frame())
  autosize_excel_columns_df(worksheet, df, offset=df.index.nlevels)


# CALL
file_name = 'abc.xlsx'
data_sheet = ''
df_sheet = pd.DataFrame(data_sheet)
sheet_name = ''
with pd.ExcelWriter(file_name) as writer:
    df_sheet.to_excel(
        writer,
        sheet_name=sheet_name,
        index=True,
        index_label='No.',
        header=True,
        freeze_panes=(1, 1)
    )
# FIT WIDTH COLUMNS
worksheet = writer.sheets[sheet_name]
autosize_excel_columns(worksheet, df_sheet)
# - AUTO FIT COLUMN EXCEL FILE : END -------------------------------------------------------------------