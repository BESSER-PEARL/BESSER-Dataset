





import java.util.List;
import java.util.ArrayList;

public class behaviour_TaskExecution extends NamedElement {

    private String status;





    private behaviour_DynamicRobot behaviour_dynamicrobot;




    private List<behaviour_DynamicRobot> behaviour_dynamicrobots;




    private behaviour_BehaviourContainer behaviour_behaviourcontainer;


    public behaviour_TaskExecution(
        String status    ) {
        super(
        );
        this.status = status;
        this.behaviour_dynamicrobots = new ArrayList<>();
    }

    public behaviour_TaskExecution(
        String status        ArrayList<behaviour_DynamicRobot> behaviour_dynamicrobots    ) {
        this.status = status;
        this.behaviour_dynamicrobots = behaviour_dynamicrobots;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }
    public List<behaviour_DynamicRobot> getBehaviour_dynamicrobots() {
        return behaviour_dynamicrobots;
    }

    public void addBehaviour_dynamicrobot(Behaviour_dynamicrobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobots.add(behaviour_dynamicrobot);
    }
    public behaviour_BehaviourContainer getBehaviour_behaviourcontainer() {
        return behaviour_behaviourcontainer;
    }

    public void setBehaviour_behaviourcontainer(behaviour_BehaviourContainer behaviour_behaviourcontainer) {
        this.behaviour_behaviourcontainer = behaviour_behaviourcontainer;
    }

}