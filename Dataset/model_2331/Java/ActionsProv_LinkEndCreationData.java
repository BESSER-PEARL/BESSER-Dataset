





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_LinkEndCreationData extends LinkEndData {

    private boolean isReplaceAll;





    private ActionsProv_InputPin actionsprov_inputpin;


    public ActionsProv_LinkEndCreationData(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public ActionsProv_InputPin getActionsprov_inputpin() {
        return actionsprov_inputpin;
    }

    public void setActionsprov_inputpin(ActionsProv_InputPin actionsprov_inputpin) {
        this.actionsprov_inputpin = actionsprov_inputpin;
    }

}