





import java.util.List;
import java.util.ArrayList;

public class droneDSL_PourcentConst extends PourcentExp {

    private String val;





    private droneDSL_Pourcent_vitesse_hauteur_max dronedsl_pourcent_vitesse_hauteur_max;


    public droneDSL_PourcentConst(
        String val    ) {
        super(
        );
        this.val = val;
    }


    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public droneDSL_Pourcent_vitesse_hauteur_max getDronedsl_pourcent_vitesse_hauteur_max() {
        return dronedsl_pourcent_vitesse_hauteur_max;
    }

    public void setDronedsl_pourcent_vitesse_hauteur_max(droneDSL_Pourcent_vitesse_hauteur_max dronedsl_pourcent_vitesse_hauteur_max) {
        this.dronedsl_pourcent_vitesse_hauteur_max = dronedsl_pourcent_vitesse_hauteur_max;
    }

}