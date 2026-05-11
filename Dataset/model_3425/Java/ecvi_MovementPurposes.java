





import java.util.List;
import java.util.ArrayList;

public class ecvi_MovementPurposes  {

    private String movementPurpose;





    private ecvi_Ecvi ecvi_ecvi;


    public ecvi_MovementPurposes(
        String movementPurpose    ) {
        this.movementPurpose = movementPurpose;
    }


    public String getMovementpurpose() {
        return movementPurpose;
    }

    public void setMovementpurpose(String movementPurpose) {
        this.movementPurpose = movementPurpose;
    }

    public ecvi_Ecvi getEcvi_ecvi() {
        return ecvi_ecvi;
    }

    public void setEcvi_ecvi(ecvi_Ecvi ecvi_ecvi) {
        this.ecvi_ecvi = ecvi_ecvi;
    }

}