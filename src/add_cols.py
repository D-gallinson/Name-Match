import pandas as pd


class AddCols():
	def __init__(self, adder_df, addee_df, adder_id, addee_id):
		self.addee_df = addee_df
		self.addee_id = addee_id
		self.addee_id_vec = addee_df[addee_id]

		self.adder_df = adder_df
		self.adder_id = adder_id
		self.adder_id_vec = adder_df[adder_id]


	def head(self, rows=5):
		print(self.addee_df.head(rows))


	def add_cols(self, *add_col_list):
		adder_df = self.adder_df.set_index(self.adder_id_vec)

		for col in add_col_list:
			col_to_add = adder_df[col]
			self.addee_df[col] = self.addee_df[self.addee_id].map(col_to_add)

		return self.addee_df