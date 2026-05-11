





import java.util.List;
import java.util.ArrayList;

public class smalluml_Methode extends ElementNomme {

    private boolean methodeAbstraite;





    private smalluml_Classe smalluml_classe;


    public smalluml_Methode(
        boolean methodeAbstraite    ) {
        super(
        );
        this.methodeAbstraite = methodeAbstraite;
    }


    public boolean getMethodeabstraite() {
        return methodeAbstraite;
    }

    public void setMethodeabstraite(boolean methodeAbstraite) {
        this.methodeAbstraite = methodeAbstraite;
    }

    public smalluml_Classe getSmalluml_classe() {
        return smalluml_classe;
    }

    public void setSmalluml_classe(smalluml_Classe smalluml_classe) {
        this.smalluml_classe = smalluml_classe;
    }

}