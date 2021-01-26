import pandas as pd
from add_cols import AddCols
import sys
sys.path.insert(1, 'C:\\Users\\Dylan\\OneDrive\\Documents\\Programming\\Research\\Parse_GTF')
from parse_gtf import ParseGTF


def run(**args):
	print("Reading GTF file...", end="")
	gtf = ParseGTF(args['gtf_path'])
	print("done!")

	if args['feature']:
		gtf.filter_feature(args['feature'], inplace=True)

	print("Parsing attribute columns...", end="")
	gtf.parse_attribute(replace_att=True)
	gtf.clean_quotes()
	print("done!")

	if 'locus' in args['cols_to_add']:
		gtf.add_col('locus', gtf.full_locus())

	gtf_df = gtf()
	gtf_df.drop_duplicates(args['gtf_id_col'], inplace=True)

	print("Reading target file...", end="")
	target_df = read_dynamic(args['target_path'])
	print("done!")

	print("Adding columns to target file...", end="")
	match_obj = AddCols(gtf_df, target_df, args['gtf_id_col'], args['input_id_col'])
	output_df = match_obj.add_cols(*args['cols_to_add'])
	print("done!")

	output_df.to_csv(args['output'], index=False)
	print(f"Output written to: {args['output']}")


def read_dynamic(path):
	ext = path[path.rfind(".")+1:]
	if ext == "csv":
		df = pd.read_csv(path)
	elif ext == "tabular":
		df = pd.read_table(path)
	else:
		df = pd.read_excel(path)

	return df