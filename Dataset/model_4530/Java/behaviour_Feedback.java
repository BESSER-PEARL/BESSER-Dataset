





import java.util.List;
import java.util.ArrayList;

public class behaviour_Feedback extends CommunicationAction {

    private String actionName;



    public behaviour_Feedback(
        String actionName    ) {
        super(
        );
        this.actionName = actionName;
    }


    public String getActionname() {
        return actionName;
    }

    public void setActionname(String actionName) {
        this.actionName = actionName;
    }


}