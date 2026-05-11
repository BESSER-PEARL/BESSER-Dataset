





import java.util.List;
import java.util.ArrayList;

public class cbpmn_OCLConstraint  {

    private String constraintStr;
    private String constraintName;





    private cbpmn_ProcessModel cbpmn_processmodel;


    public cbpmn_OCLConstraint(
        String constraintStr,        String constraintName    ) {
        this.constraintStr = constraintStr;
        this.constraintName = constraintName;
    }


    public String getConstraintstr() {
        return constraintStr;
    }

    public void setConstraintstr(String constraintStr) {
        this.constraintStr = constraintStr;
    }
    public String getConstraintname() {
        return constraintName;
    }

    public void setConstraintname(String constraintName) {
        this.constraintName = constraintName;
    }

    public cbpmn_ProcessModel getCbpmn_processmodel() {
        return cbpmn_processmodel;
    }

    public void setCbpmn_processmodel(cbpmn_ProcessModel cbpmn_processmodel) {
        this.cbpmn_processmodel = cbpmn_processmodel;
    }

}