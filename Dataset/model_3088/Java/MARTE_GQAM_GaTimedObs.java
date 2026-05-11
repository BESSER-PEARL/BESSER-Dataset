





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaTimedObs extends NfpConstraint {

    private String laxity;



    public MARTE_GQAM_GaTimedObs(
        String laxity    ) {
        super(
        );
        this.laxity = laxity;
    }


    public String getLaxity() {
        return laxity;
    }

    public void setLaxity(String laxity) {
        this.laxity = laxity;
    }


}