





import java.util.List;
import java.util.ArrayList;

public class simulink_stateflow_Transition extends StateflowElement {

    private int priority;



    public simulink_stateflow_Transition(
        int priority    ) {
        super(
        );
        this.priority = priority;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }


}