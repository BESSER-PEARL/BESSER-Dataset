





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlIsFunctional extends SadlPropertyRestriction {

    private boolean inverse;



    public sADL_SadlIsFunctional(
        boolean inverse    ) {
        super(
        );
        this.inverse = inverse;
    }


    public boolean getInverse() {
        return inverse;
    }

    public void setInverse(boolean inverse) {
        this.inverse = inverse;
    }


}