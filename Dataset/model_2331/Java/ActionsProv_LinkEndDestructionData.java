





import java.util.List;
import java.util.ArrayList;

public class ActionsProv_LinkEndDestructionData extends LinkEndData {

    private boolean isDestroyDuplicates;





    private ActionsProv_InputPin actionsprov_inputpin;


    public ActionsProv_LinkEndDestructionData(
        boolean isDestroyDuplicates    ) {
        super(
        );
        this.isDestroyDuplicates = isDestroyDuplicates;
    }


    public boolean getIsdestroyduplicates() {
        return isDestroyDuplicates;
    }

    public void setIsdestroyduplicates(boolean isDestroyDuplicates) {
        this.isDestroyDuplicates = isDestroyDuplicates;
    }

    public ActionsProv_InputPin getActionsprov_inputpin() {
        return actionsprov_inputpin;
    }

    public void setActionsprov_inputpin(ActionsProv_InputPin actionsprov_inputpin) {
        this.actionsprov_inputpin = actionsprov_inputpin;
    }

}