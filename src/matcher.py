import time
import main
import argparse as ag


parser = ag.ArgumentParser(description="Add information to a delimited file from a GTF file by matching a column shared between the two files.")
parser.add_argument("-i", "--input", dest="target_path", required=True, help="Path to the file to add columns to")
parser.add_argument("-g", "--gtf", dest="gtf_path", required=True, help="Path to the GTF file used to add columns to the input file")
parser.add_argument("-ii", "--input_id", dest="input_id_col", required=True, help="Name of the input id column to match")
parser.add_argument("-gi", "--gtf_id", dest="gtf_id_col", required=True, help="Name of the GTF id column to match")
parser.add_argument("-a", "--add_cols", dest="cols_to_add", nargs="+", required=True, help="List of column names from the GTF file to add to the target file")
parser.add_argument("-f", "--filer_feature", dest="feature", default="transcript", help="Feature in the \"feature\" column of the GTF file by which to filter the file by. Greatly increases speed. If no feature is desired, use: \"\" or None")
parser.add_argument("-o", "--output", dest="output", default="matched_out.csv", help="Output file path")

args = parser.parse_args()

if args.feature.upper() == "NONE":
	feature = None
else:
	feature = args.feature

arg_dict = {
	'target_path': args.target_path,
	'gtf_path': args.gtf_path,
	'input_id_col': args.input_id_col,
	'gtf_id_col': args.gtf_id_col,
	'cols_to_add': args.cols_to_add,
	'feature': feature,
	'output': args.output
}

start = time.perf_counter()
main.run(**arg_dict)
delta = time.perf_counter() - start
print("Total execution time: %.5fs" % delta)