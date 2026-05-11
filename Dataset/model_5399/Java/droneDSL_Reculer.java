





import java.util.List;
import java.util.ArrayList;

public class droneDSL_Reculer extends CommandeBasique, Mouvement, AR {






    private droneDSL_SecondeExp dronedsl_secondeexp;




    private droneDSL_PourcentExp dronedsl_pourcentexp;


    public droneDSL_Reculer(
    ) {
        super(
        );
    }



    public droneDSL_SecondeExp getDronedsl_secondeexp() {
        return dronedsl_secondeexp;
    }

    public void setDronedsl_secondeexp(droneDSL_SecondeExp dronedsl_secondeexp) {
        this.dronedsl_secondeexp = dronedsl_secondeexp;
    }
    public droneDSL_PourcentExp getDronedsl_pourcentexp() {
        return dronedsl_pourcentexp;
    }

    public void setDronedsl_pourcentexp(droneDSL_PourcentExp dronedsl_pourcentexp) {
        this.dronedsl_pourcentexp = dronedsl_pourcentexp;
    }

}