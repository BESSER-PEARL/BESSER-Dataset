





import java.util.List;
import java.util.ArrayList;

public class behaviour_MessageRepository extends NamedElement {






    private behaviour_DynamicRobot behaviour_dynamicrobot;




    private List<behaviour_Message> behaviour_messages;




    private behaviour_DynamicRobot behaviour_dynamicrobot;




    private List<behaviour_Message> behaviour_messages;


    public behaviour_MessageRepository(
    ) {
        super(
        );
        this.behaviour_messages = new ArrayList<>();
        this.behaviour_messages = new ArrayList<>();
    }

    public behaviour_MessageRepository(
        ArrayList<behaviour_Message> behaviour_messages,        ArrayList<behaviour_Message> behaviour_messages    ) {
        this.behaviour_messages = behaviour_messages;
        this.behaviour_messages = behaviour_messages;
    }


    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }
    public List<behaviour_Message> getBehaviour_messages() {
        return behaviour_messages;
    }

    public void addBehaviour_message(Behaviour_message behaviour_message) {
        this.behaviour_messages.add(behaviour_message);
    }
    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }
    public List<behaviour_Message> getBehaviour_messages() {
        return behaviour_messages;
    }

    public void addBehaviour_message(Behaviour_message behaviour_message) {
        this.behaviour_messages.add(behaviour_message);
    }

}