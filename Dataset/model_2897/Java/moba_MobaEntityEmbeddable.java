





import java.util.List;
import java.util.ArrayList;

public class moba_MobaEntityEmbeddable extends MobaEntityFeature, MobaMultiplicityAble {

    private boolean transient;





    private moba_MobaEntity moba_mobaentity;


    public moba_MobaEntityEmbeddable(
        boolean transient    ) {
        super(
        );
        this.transient = transient;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public moba_MobaEntity getMoba_mobaentity() {
        return moba_mobaentity;
    }

    public void setMoba_mobaentity(moba_MobaEntity moba_mobaentity) {
        this.moba_mobaentity = moba_mobaentity;
    }

}