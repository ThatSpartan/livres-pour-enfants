package {
	
	// importer display et events
	import flash.display.*;
	import flash.events.*;

    public class U3A3_Livres extends MovieClip
    {
		
		// créer la tables pour contenir la liste des livres
		var livre:Array = new Array();

        // fonction contructeur
        public function U3A3_Livres()
        {
            
            // ajouter les écouteurs d'événements
			btnAfficher.addEventListener(MouseEvent.CLICK, afficher);
			
			// ajouter le fichier U3A3_FichierDeLivres.as
			include "U3A3_FichierDeLivres.as";

        }
		
		// fonction pour afficher si le livre est là ou non
		public function afficher(EVENT:MouseEvent):void
		{
			
			var ref:int = int(txtRef.text);
			
			// afficher le nom du livre
			// appeler la fonction de recherche
			txtAfficher.text = rechercheBinaire(livre, ref)
			
			// effacer la boite de saisie
			txtRef.text = '';
			
		}

        // fonction pour la recherche binaire
        public function rechercheBinaire(arr:Array, val:int):String
        {
            
            // si l'array est vide : il reste aucune valeur
            // si l'array contient un seul élément et ce n'est pas celui recherché
            // donc valeur recherché n'existe pas
            if (arr.length == 0 || (arr.length == 1 && arr[0][0] != val))
            {
                return 'Le livre n\'existe pas';
            }

            var nombreElements:int = arr.length / 2;
            var valMilieu:int = arr[nombreElements][0];

            if (val == valMilieu)
            {
                return 'Le livre est ' + arr[nombreElements][1];
            }
            else if (val < valMilieu)   // valeur est plus petite
            {
                return rechercheBinaire(arr.slice(0, nombreElements), val);
            }
            else if (val > valMilieu)   // valeur est plus grande
            {
                return rechercheBinaire(arr.slice(nombreElements+1, -1), val);
            }
			
			return 'Erreur';

        }

    }

}