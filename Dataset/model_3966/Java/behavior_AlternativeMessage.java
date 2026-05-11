





import java.util.List;
import java.util.ArrayList;

public class behavior_AlternativeMessage extends Message {






    private List<behavior_Message> behavior_messages;


    public behavior_AlternativeMessage(
    ) {
        super(
        );
        this.behavior_messages = new ArrayList<>();
    }

    public behavior_AlternativeMessage(
        ArrayList<behavior_Message> behavior_messages    ) {
        this.behavior_messages = behavior_messages;
    }


    public List<behavior_Message> getBehavior_messages() {
        return behavior_messages;
    }

    public void addBehavior_message(Behavior_message behavior_message) {
        this.behavior_messages.add(behavior_message);
    }

}