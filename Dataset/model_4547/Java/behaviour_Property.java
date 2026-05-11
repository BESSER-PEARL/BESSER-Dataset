





import java.util.List;
import java.util.ArrayList;

public class behaviour_Property  {






    private behaviour_Message behaviour_message;




    private behaviour_TaskRequirement behaviour_taskrequirement;




    private behaviour_Action behaviour_action;


    public behaviour_Property(
    ) {
    }



    public behaviour_Message getBehaviour_message() {
        return behaviour_message;
    }

    public void setBehaviour_message(behaviour_Message behaviour_message) {
        this.behaviour_message = behaviour_message;
    }
    public behaviour_TaskRequirement getBehaviour_taskrequirement() {
        return behaviour_taskrequirement;
    }

    public void setBehaviour_taskrequirement(behaviour_TaskRequirement behaviour_taskrequirement) {
        this.behaviour_taskrequirement = behaviour_taskrequirement;
    }
    public behaviour_Action getBehaviour_action() {
        return behaviour_action;
    }

    public void setBehaviour_action(behaviour_Action behaviour_action) {
        this.behaviour_action = behaviour_action;
    }

}