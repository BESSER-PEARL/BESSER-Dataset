





import java.util.List;
import java.util.ArrayList;

public class smalluml_Attribut extends ElementNomme {






    private smalluml_Methode smalluml_methode;




    private smalluml_TypeDonnee smalluml_typedonnee;




    private smalluml_Classe smalluml_classe;


    public smalluml_Attribut(
    ) {
        super(
        );
    }



    public smalluml_Methode getSmalluml_methode() {
        return smalluml_methode;
    }

    public void setSmalluml_methode(smalluml_Methode smalluml_methode) {
        this.smalluml_methode = smalluml_methode;
    }
    public smalluml_TypeDonnee getSmalluml_typedonnee() {
        return smalluml_typedonnee;
    }

    public void setSmalluml_typedonnee(smalluml_TypeDonnee smalluml_typedonnee) {
        this.smalluml_typedonnee = smalluml_typedonnee;
    }
    public smalluml_Classe getSmalluml_classe() {
        return smalluml_classe;
    }

    public void setSmalluml_classe(smalluml_Classe smalluml_classe) {
        this.smalluml_classe = smalluml_classe;
    }

}