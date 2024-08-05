To jest EDA danych związych z powikłaniami serca oraz próba modelowania klasyfikacyjnego:

W pliku eda.ipynb znajduję się kod analiza danych wraz z modelami.
Użyto 9 różnych modeli klasyfikacyjnych

KNeighborsClassifier()
LogisticRegression()
RandomForestClassifier()
GradientBoostingClassifier()
AdaBoostClassifier()
HistGradientBoostingClassifier()
XGBClassifier()
LGBMClassifier(verbose = -1)
CatBoostClassifier(verbose=0)

Plik app.py jest aplikcają internetową w której można przeglądać dane wejściowe, modele oraz wykresy z nimi związane.

-- streamlit app.py
