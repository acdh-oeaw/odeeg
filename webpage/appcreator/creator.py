import ast
import pandas as pd
from jinja2 import Template
from . import code_templates


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
                    field_type = row['field type'].split('|')[0]
                    if field_type == 'FK':
                        field['field_type'] = 'ForeignKey'
                    else:
                        field['field_type'] = 'ManyToManyField'
                    field['related_class'] = row['field type'].split('|')[1].split(':')[0]
                    field['related_name'] = "rvn_{}_{}_{}".format(
                        x[0].lower(),
                        field_name,
                        field['related_class'].lower()
                    )
                elif row['field type'] == "URI":
                    field['field_type'] = "CharField"
                elif row['field type'] == "Boolean":
                    field['field_type'] = "BooleanField"
                elif row['field type'] == "ChoiceField":
                    if isinstance(row['choices'], str):
                        field['choices'] = ast.literal_eval(row['choices'])
                    field['field_type'] = "CharField"
                else:
                    field['field_type'] = row['field type']
                if isinstance(row['verbose field name'], str):
                    field['field_verbose_name'] = row['verbose field name']
                if isinstance(row['helptext'], str):
                    field['field_helptext'] = row['helptext']

                class_dict['model_fields'].append(field)
        yield class_dict


def serialize_data_model(dicts, app_name="my_sirad_app", file_name='output_model.py'):
    t = Template(code_templates.MODELS_PY)
    output = t.render(
        data=dicts,
        app_name=app_name
    )
    with open(file_name, "w") as text_file:
        print(output, file=text_file)
    return output
