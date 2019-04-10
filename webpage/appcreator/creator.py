import pandas as pd


def xlsx_to_classdicts(file):
    """
    parses an Excel sheet and yields dicts of model definitions
    :param file: path to an Excel sheet
    :return: yields dicts
    """
    df = pd.read_excel(file)
    classes = df.groupby('class name technical')
    for x in classes:
        local_df = x[1]
        class_dict = {}
        class_dict['model_name'] = x[0]
        class_dict['model_helptext'] = df['class name helptext'].iloc[0]
        class_dict['model_verbose_name'] = df['class name verbose_name'].iloc[0]
        class_dict['model_fields'] = []
        for i, row in local_df.iterrows():
            field_name = row['field name technical']
            if isinstance(field_name, str) and isinstance(row['field type'], str):
                field = {}
                field['field_name'] = field_name
                if '|' in row['field type']:
                    field['field_type'] = row['field type'].split('|')[0]
                    field['related_class'] = row['field type'].split('|')[1]
                else:
                    field['field_type'] = row['field type']
                if isinstance(row['verbose field name'], str):
                    field['field_verbose_name'] = row['verbose field name']
                if isinstance(row['helptext'], str):
                    field['field_helptext'] = row['helptext']

                class_dict['model_fields'].append(field)
        yield class_dict
