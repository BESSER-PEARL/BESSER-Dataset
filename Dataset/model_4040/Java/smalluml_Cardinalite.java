





import java.util.List;
import java.util.ArrayList;

public class smalluml_Cardinalite extends ElementNomme {

    private String multipliciteInf;
    private String multipliciteSup;





    private smalluml_Association smalluml_association;




    private smalluml_Classe smalluml_classe;


    public smalluml_Cardinalite(
        String multipliciteInf,        String multipliciteSup    ) {
        super(
        );
        this.multipliciteInf = multipliciteInf;
        this.multipliciteSup = multipliciteSup;
    }


    public String getMultipliciteinf() {
        return multipliciteInf;
    }

    public void setMultipliciteinf(String multipliciteInf) {
        this.multipliciteInf = multipliciteInf;
    }
    public String getMultiplicitesup() {
        return multipliciteSup;
    }

    public void setMultiplicitesup(String multipliciteSup) {
        this.multipliciteSup = multipliciteSup;
    }

    public smalluml_Association getSmalluml_association() {
        return smalluml_association;
    }

    public void setSmalluml_association(smalluml_Association smalluml_association) {
        this.smalluml_association = smalluml_association;
    }
    public smalluml_Classe getSmalluml_classe() {
        return smalluml_classe;
    }

    public void setSmalluml_classe(smalluml_Classe smalluml_classe) {
        this.smalluml_classe = smalluml_classe;
    }

}