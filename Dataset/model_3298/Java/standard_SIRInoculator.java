





import java.util.List;
import java.util.ArrayList;

public class standard_SIRInoculator extends SIInfector {

    private float inoculatedPercentage;
    private boolean inoculatePercentage;



    public standard_SIRInoculator(
        float inoculatedPercentage,        boolean inoculatePercentage    ) {
        super(
        );
        this.inoculatedPercentage = inoculatedPercentage;
        this.inoculatePercentage = inoculatePercentage;
    }


    public float getInoculatedpercentage() {
        return inoculatedPercentage;
    }

    public void setInoculatedpercentage(float inoculatedPercentage) {
        this.inoculatedPercentage = inoculatedPercentage;
    }
    public boolean getInoculatepercentage() {
        return inoculatePercentage;
    }

    public void setInoculatepercentage(boolean inoculatePercentage) {
        this.inoculatePercentage = inoculatePercentage;
    }


}