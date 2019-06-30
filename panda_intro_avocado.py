import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('avocado.csv')
# on récupére qui les types ograniques
df = df.copy()[df['type']=='organic']

df['Date'] = pd.to_datetime(df["Date"])
df.sort_values(by="Date",ascending=True,inplace=True)
graph_df = pd.DataFrame()

for region in df["region"].unique() :
	# on copie toutes les informations d'une region dans un dataFrame
	region_df = df.copy()[df['region']==region]
	# on met la date comme index
	region_df.set_index("Date",inplace=True)
	# on fait un trie par index
	region_df.sort_index(inplace=True)
	# on crée une colone spécifique a la region dans la quelle on vas stocker
	# la moyenne de chaque 25 prix
	region_df[f'{region}_price25mean'] = region_df['AveragePrice'].rolling(25).mean()
	# si on a aucune colone dans graphe_df on fait directe une afectation dans se cas on auras
	# un dataFrame avec une seule colone selui de la premiére region parcourue
	if graph_df.empty :
		# note ====> quand on recupére des colones d'un dataframe dans un autre on récupére 
		# automatiquement ses index
		graph_df = region_df[[f'{region}_price25mean']]
	# si non on join les colones existantes a la nouvelle colone
	else :
		graph_df = graph_df.join(region_df[f'{region}_price25mean'])
print(graph_df.head())
graph_df.dropna().plot()
plt.show()