// precondition: Le tableau T est trié par ordre alphabétique.

      // paramètres: T - le tableau trié.

      //             gauche - l'indice de l'élément à la gauche du 

      //                      tableau (le plus petit).

      //             droite - l'indice de l'élément à la droite du

      //                      tableau (le plus grand).

      //             V - la valeur à retrouver dans le tableau.

      function rechercheBinaire

                  (T:Array,gauche:int,droite:int,V:Object):Boolean 

        {

        var  milieu:int;  // l'indice de l'élément au centre du

        // tableau sur lequel porte la recherche.

        if (gauche > droite) 

        {

        return false;

        }

        milieu = (gauche + droite) / 2;

        if (T[milieu] == V) 

        {

        return true;

        }

        if (V < T[milieu]) 

        {

        return rechercheBinaire(T,gauche,milieu-1,V);

        }

        else 

        {

        return rechercheBinaire(T,milieu+1,droite,V);

        }

        } // Fin fonction rechercheBinaire.