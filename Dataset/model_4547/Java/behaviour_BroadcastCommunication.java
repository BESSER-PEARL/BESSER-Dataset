





import java.util.List;
import java.util.ArrayList;

public class behaviour_BroadcastCommunication extends CommunicationAction {






    private List<behaviour_DynamicRobot> behaviour_dynamicrobots;


    public behaviour_BroadcastCommunication(
    ) {
        super(
        );
        this.behaviour_dynamicrobots = new ArrayList<>();
    }

    public behaviour_BroadcastCommunication(
        ArrayList<behaviour_DynamicRobot> behaviour_dynamicrobots    ) {
        this.behaviour_dynamicrobots = behaviour_dynamicrobots;
    }


    public List<behaviour_DynamicRobot> getBehaviour_dynamicrobots() {
        return behaviour_dynamicrobots;
    }

    public void addBehaviour_dynamicrobot(Behaviour_dynamicrobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobots.add(behaviour_dynamicrobot);
    }

}