





import java.util.List;
import java.util.ArrayList;

public class behaviour_DeviceAction extends Action {

    private String actionName;



    public behaviour_DeviceAction(
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