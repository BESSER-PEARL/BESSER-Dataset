





import java.util.List;
import java.util.ArrayList;

public class dataflownet_StateMachineTransition extends NamedElement {

    private int priority;



    public dataflownet_StateMachineTransition(
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