





import java.util.List;
import java.util.ArrayList;

public class uml_DecisionNode extends ControlNode {






    private uml_Behavior uml_behavior;




    private uml_ObjectFlow uml_objectflow;


    public uml_DecisionNode(
    ) {
        super(
        );
    }



    public uml_Behavior getUml_behavior() {
        return uml_behavior;
    }

    public void setUml_behavior(uml_Behavior uml_behavior) {
        this.uml_behavior = uml_behavior;
    }
    public uml_ObjectFlow getUml_objectflow() {
        return uml_objectflow;
    }

    public void setUml_objectflow(uml_ObjectFlow uml_objectflow) {
        this.uml_objectflow = uml_objectflow;
    }

}