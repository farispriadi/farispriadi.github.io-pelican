from jinja2 import Environment, FileSystemLoader
import os
import sys
import numpy as np
import pandas as pd



def create_dataframe(filename="data/pengeluaran_sayur_bulanan_jateng.csv"):
    """Create Pandas DataFrame from local CSV."""
    """ Persentase Pengeluaran per Kapita Sebulan Jawa Tengah 2018-2021 """
    df = pd.read_csv(filename)
    return df

def generate_markdown(template_filename='sayur.jinja2', dataframe=pd.DataFrame()):
	root = os.path.dirname(os.path.abspath(__file__))
	templates_dir = os.path.join(root, 'chartjs_templates')
	env = Environment( loader = FileSystemLoader(templates_dir) )
	template = env.get_template(template_filename)
	 
	 
	filename = os.path.join(root, 'content', template_filename.replace('.jinja2','.md'))
	with open(filename, 'w') as fh:
	    fh.write(template.render(
			x_values = dataframe[dataframe.columns[0]],
			y_values = dataframe[dataframe.columns[1]]
	    ))

if __name__ == '__main__':
	if len(sys.argv) >=3:
		generate_markdown(sys.argv[1],create_dataframe(sys.argv[2]))
	else:
		generate_markdown(dataframe=create_dataframe())