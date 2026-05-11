





import java.util.List;
import java.util.ArrayList;

public class CommonBehavior_BasicBehavior_Behavior extends Class {

    private boolean isReentrant;





    private List<Behavior> behaviors;


    public CommonBehavior_BasicBehavior_Behavior(
        boolean isReentrant    ) {
        super(
        );
        this.isReentrant = isReentrant;
        this.behaviors = new ArrayList<>();
    }

    public CommonBehavior_BasicBehavior_Behavior(
        boolean isReentrant        ArrayList<Behavior> behaviors    ) {
        this.isReentrant = isReentrant;
        this.behaviors = behaviors;
    }

    public boolean getIsreentrant() {
        return isReentrant;
    }

    public void setIsreentrant(boolean isReentrant) {
        this.isReentrant = isReentrant;
    }

    public List<Behavior> getBehaviors() {
        return behaviors;
    }

    public void addBehavior(Behavior behavior) {
        this.behaviors.add(behavior);
    }

}