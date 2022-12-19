# Indexation
`language : French`
### Methode : Indexation inversé
-- Lire --
l'objectif est de rechercher des mots-clés dans un grand nombre de documents ou corpus.
 
| Language utilisé | Bibliothèques  | 	Scripts			 | 
|-------- | ---------- | --------------- | ---------- |
| Python  | **pickle**--**os**--**sys** 	 	 | `pickling.py`/`main.py` |

---

### Installation et configuration

> vous devez installer pipenv un gestionnaire d'environnement pour Python

 - `git clone` *repo*
 - `pipenv shell` *(lancement de l'environnement python)*
 - `cd src`

### Essais

> Cette section sera mise à jour.
 - `python pickling.py ../documents` *(créer un index inversé et le stocker dans un fichier binaire)*
 - `python main.py "query"` *(query expl : hello and cool)*


### analyse

> `pickling.py`

    
    if __name__ == "__main__":

    """
    pickle the list files containing words into a binary format of an inverted index
    """

    # arg_1 -> chemin du répertoire qui contient la liste des documents
    arg_1 = sys.argv[1]
    while not check_arg(arg_1):
        print("Please provide appropriate arguments")
        arg_1 = input("Provide directory path : ")

    index = IndexUtil(arg_1)

    # récupérer les documents inversés à partir de l'index dans pickle.pkl
    print(f"{len(index.doc.keys())} WORDS \n")

    with open("./pickle.pkl", "wb") as pkl:
        pickle.dump(index.doc, pkl)
	 

> `main.py`

    if __name__ == "__main__":
    # arg_1 -> requête
    arg_1 = sys.argv[1]
	
	# récupérer les information du fichier pickle.pkl et rechercher ensuite dans l'index
    search_obj = SearchInvertedIndex("./pickle.pkl", arg_1)
	# affichage du resultat
    print(search_obj.search_index())
----------    

#### SearchInvertedIndex Class

[SearchInvertedIndex Class #1](./images/hello.png)

[SearchInvertedIndex Class #2](./images/hello1.png)

----------

#### QueryMixin Class
[QueryMixin Class](./images/hello2.png)

	

