





import java.util.List;
import java.util.ArrayList;

public class cbpmn_OCLConstraint  {

    private String constraintName;
    private String constraintStr;





    private cbpmn_Branch cbpmn_branch;




    private cbpmn_Branch cbpmn_branch;




    private cbpmn_ProcessModel cbpmn_processmodel;


    public cbpmn_OCLConstraint(
        String constraintName,        String constraintStr    ) {
        this.constraintName = constraintName;
        this.constraintStr = constraintStr;
    }


    public String getConstraintname() {
        return constraintName;
    }

    public void setConstraintname(String constraintName) {
        this.constraintName = constraintName;
    }
    public String getConstraintstr() {
        return constraintStr;
    }

    public void setConstraintstr(String constraintStr) {
        this.constraintStr = constraintStr;
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
    public cbpmn_ProcessModel getCbpmn_processmodel() {
        return cbpmn_processmodel;
    }

    public void setCbpmn_processmodel(cbpmn_ProcessModel cbpmn_processmodel) {
        this.cbpmn_processmodel = cbpmn_processmodel;
    }

}