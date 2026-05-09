





import java.util.List;
import java.util.ArrayList;

public class StateMachines_BehaviorStateMachines_Transition extends BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement {

    private String kind;





    private Region region;




    private Behavior behavior;


    public StateMachines_BehaviorStateMachines_Transition(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Region getRegion() {
        return region;
    }

    public void setRegion(Region region) {
        this.region = region;
    }
    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        this.behavior = behavior;
    }

}