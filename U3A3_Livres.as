package {

    public class U3A3_Livres extends MovieClip
    {

        // fonction contructeur
        public function U3A3_Livres()
        {
            
            // ajouter les écouteurs d'événements

            

        }

        // fonction pour la recherche binaire
        public function rechercheBinaire(arr:Array, val:int):String
        {
            
            // si l'array est vide : il reste aucune valeur
            // si l'array contient un seul élément et ce n'est pas celui recherché
            // donc valeur recherché n'existe pas
            if (arr.length == 0 || (arr.length == 1 && arr[0][0] != val))
            {
                return false;
            }

            var nombreElements:int = arr.length / 2;
            var valMilieu:int = arr[nombreElements][0];

            if (val == valMilieu)
            {
                return arr[nombreElements][1];
            }
            else if (val < valMilieu)   // valeur est plus petite
            {
                return rechercheBinaire(arr.slice(0, nombreElements), val);
            }
            else if (val > valMilieu)   // valeur est plus grande
            {
                return rechercheBinaire(arr.slice(nombreElements+1, -1), val);
            }

        }

    }

}