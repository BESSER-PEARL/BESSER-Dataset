





import java.util.List;
import java.util.ArrayList;

public class UMLModel_DecisionNode extends ControlNode {

    private String decisionInput;



    public UMLModel_DecisionNode(
        String decisionInput    ) {
        super(
        );
        this.decisionInput = decisionInput;
    }


    public String getDecisioninput() {
        return decisionInput;
    }

    public void setDecisioninput(String decisionInput) {
        this.decisionInput = decisionInput;
    }


}