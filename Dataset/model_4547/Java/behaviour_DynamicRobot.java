





import java.util.List;
import java.util.ArrayList;

public class behaviour_DynamicRobot extends NamedElement {

    private String status;





    private behaviour_BehaviourContainer behaviour_behaviourcontainer;


    public behaviour_DynamicRobot(
        String status    ) {
        super(
        );
        this.status = status;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public behaviour_BehaviourContainer getBehaviour_behaviourcontainer() {
        return behaviour_behaviourcontainer;
    }

    public void setBehaviour_behaviourcontainer(behaviour_BehaviourContainer behaviour_behaviourcontainer) {
        this.behaviour_behaviourcontainer = behaviour_behaviourcontainer;
    }

}