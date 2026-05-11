





import java.util.List;
import java.util.ArrayList;

public class droneDSL_SecondeConst extends SecondeExp {

    private String val;





    private droneDSL_Hauteur_max dronedsl_hauteur_max;


    public droneDSL_SecondeConst(
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

    public droneDSL_Hauteur_max getDronedsl_hauteur_max() {
        return dronedsl_hauteur_max;
    }

    public void setDronedsl_hauteur_max(droneDSL_Hauteur_max dronedsl_hauteur_max) {
        this.dronedsl_hauteur_max = dronedsl_hauteur_max;
    }

}