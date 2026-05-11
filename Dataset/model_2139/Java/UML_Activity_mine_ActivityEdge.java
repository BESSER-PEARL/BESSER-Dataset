





import java.util.List;
import java.util.ArrayList;

public class UML_Activity_mine_ActivityEdge extends Element {

    private boolean objectFlow;





    private UML_Activity_mine_Activity uml_activity_mine_activity;


    public UML_Activity_mine_ActivityEdge(
        boolean objectFlow    ) {
        super(
        );
        this.objectFlow = objectFlow;
    }


    public boolean getObjectflow() {
        return objectFlow;
    }

    public void setObjectflow(boolean objectFlow) {
        this.objectFlow = objectFlow;
    }

    public UML_Activity_mine_Activity getUml_activity_mine_activity() {
        return uml_activity_mine_activity;
    }

    public void setUml_activity_mine_activity(UML_Activity_mine_Activity uml_activity_mine_activity) {
        this.uml_activity_mine_activity = uml_activity_mine_activity;
    }

}