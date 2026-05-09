





import java.util.List;
import java.util.ArrayList;

public class xmof_BasicBehaviors_Behavior extends BehavioredEClass {

    private boolean reentrant;



    public xmof_BasicBehaviors_Behavior(
        boolean reentrant    ) {
        super(
        );
        this.reentrant = reentrant;
    }


    public boolean getReentrant() {
        return reentrant;
    }

    public void setReentrant(boolean reentrant) {
        this.reentrant = reentrant;
    }


}