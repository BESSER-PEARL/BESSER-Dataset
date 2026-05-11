





import java.util.List;
import java.util.ArrayList;

public class moba_MobaSettingsEntityReference extends MobaSettingsFeature, MobaConstraintable, MobaMultiplicityAble {

    private boolean lazy;
    private boolean cascading;
    private boolean transient;



    public moba_MobaSettingsEntityReference(
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


}