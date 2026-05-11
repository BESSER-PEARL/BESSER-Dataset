





import java.util.List;
import java.util.ArrayList;

public class cbpmn_DecisionCondition extends OCLConstraint {

    private boolean isDefault;





    private cbpmn_Branch cbpmn_branch;




    private cbpmn_Branch cbpmn_branch;


    public cbpmn_DecisionCondition(
        boolean isDefault    ) {
        super(
        );
        this.isDefault = isDefault;
    }


    public boolean getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(boolean isDefault) {
        this.isDefault = isDefault;
    }

    public cbpmn_Branch getCbpmn_branch() {
        return cbpmn_branch;
    }

    public void setCbpmn_branch(cbpmn_Branch cbpmn_branch) {
        this.cbpmn_branch = cbpmn_branch;
    }
    public cbpmn_Branch getCbpmn_branch() {
        return cbpmn_branch;
    }

    public void setCbpmn_branch(cbpmn_Branch cbpmn_branch) {
        this.cbpmn_branch = cbpmn_branch;
    }

}