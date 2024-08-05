To jest EDA danych związych z powikłaniami serca oraz próba modelowania klasyfikacyjnego:
Dane zostały przeskalowane, użyto przy treningu metod redukcji wymiarowości.
W pliku eda.ipynb znajduję się kod analiza danych wraz z modelami.
Użyto 9 różnych modeli klasyfikacyjnych przy treningu
- KNeighborsClassifier
- LogisticRegression
- RandomForestClassifier
- GradientBoostingClassifier
- AdaBoostClassifier
- HistGradientBoostingClassifier
- XGBClassifier
- LGBMClassifier
- CatBoostClassifier

Modele zostały wybrane za pomocą grid serach'a.
Plik app.py jest aplikcają internetową w której można przeglądać dane wejściowe, modele oraz wykresy z nimi związane.

*Pobieranie*
- Przy pobraniu wszystkich plików
  -- pip install -r requierements.txt
  -- streamlit app.py
- Przy używaniu dockera
  -- docker build --pull --rm -f "Dockerfile" -t projekt1:latest "."
  -- docker run -p 8501:8501 projekt1 
  
