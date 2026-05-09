





import java.util.List;
import java.util.ArrayList;

public class fuml_BasicBehaviors_Behavior extends Class {

    private boolean reentrant;



    public fuml_BasicBehaviors_Behavior(
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