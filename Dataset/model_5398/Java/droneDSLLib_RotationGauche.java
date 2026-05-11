





import java.util.List;
import java.util.ArrayList;

public class droneDSLLib_RotationGauche extends Mouvement, CommandeBasique, RGRD {






    private droneDSLLib_PourcentExp dronedsllib_pourcentexp;




    private droneDSLLib_SecondeExp dronedsllib_secondeexp;


    public droneDSLLib_RotationGauche(
    ) {
        super(
        );
    }



    public droneDSLLib_PourcentExp getDronedsllib_pourcentexp() {
        return dronedsllib_pourcentexp;
    }

    public void setDronedsllib_pourcentexp(droneDSLLib_PourcentExp dronedsllib_pourcentexp) {
        this.dronedsllib_pourcentexp = dronedsllib_pourcentexp;
    }
    public droneDSLLib_SecondeExp getDronedsllib_secondeexp() {
        return dronedsllib_secondeexp;
    }

    public void setDronedsllib_secondeexp(droneDSLLib_SecondeExp dronedsllib_secondeexp) {
        this.dronedsllib_secondeexp = dronedsllib_secondeexp;
    }

}