





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_FeatureCallExp extends CallExp {

    private boolean markedPre;



    public ocl_expressions_FeatureCallExp(
        boolean markedPre    ) {
        super(
        );
        this.markedPre = markedPre;
    }


    public boolean getMarkedpre() {
        return markedPre;
    }

    public void setMarkedpre(boolean markedPre) {
        this.markedPre = markedPre;
    }


}