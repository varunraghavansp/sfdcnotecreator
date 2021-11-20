import pyodbc
import pandas as pd

class Controller:
  """
  This is a class from which one can load data from the Table.
  """

  def __init__(self, connection_string):
      """
      This is the initialization file, and it requires the connection_string.

      :param connection_string:
      :type connection_string: str
      :return:
      """

      self.connection = pyodbc.connect(connection_string)

  def query(self, query):
      """
      This function loads the data according to the query passed in query.

      :param query:
      :type query: str
      :return: dataframe
      """
      return pd.read_sql(query, self.connection)