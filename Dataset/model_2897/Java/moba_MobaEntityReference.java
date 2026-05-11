





import java.util.List;
import java.util.ArrayList;

public class moba_MobaEntityReference extends MobaEntityFeature, MobaMultiplicityAble {

    private boolean lazy;
    private boolean cascading;
    private boolean transient;





    private moba_MobaEntity moba_mobaentity;




    private moba_MobaEntityReference moba_mobaentityreference;


    public moba_MobaEntityReference(
        boolean lazy,        boolean cascading,        boolean transient    ) {
        super(
        );
        this.lazy = lazy;
        this.cascading = cascading;
        this.transient = transient;
    }


    public boolean getLazy() {
        return lazy;
    }

    public void setLazy(boolean lazy) {
        this.lazy = lazy;
    }
    public boolean getCascading() {
        return cascading;
    }

    public void setCascading(boolean cascading) {
        this.cascading = cascading;
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
    public moba_MobaEntityReference getMoba_mobaentityreference() {
        return moba_mobaentityreference;
    }

    public void setMoba_mobaentityreference(moba_MobaEntityReference moba_mobaentityreference) {
        this.moba_mobaentityreference = moba_mobaentityreference;
    }

}