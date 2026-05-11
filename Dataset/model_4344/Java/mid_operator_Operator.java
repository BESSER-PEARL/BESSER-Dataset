





import java.util.List;
import java.util.ArrayList;

public class mid_operator_Operator extends GenericElement {

    private boolean commutative;
    private String executionTime;
    private String workingPath;



    public mid_operator_Operator(
        boolean commutative,        String executionTime,        String workingPath    ) {
        super(
        );
        this.commutative = commutative;
        this.executionTime = executionTime;
        this.workingPath = workingPath;
    }


    public boolean getCommutative() {
        return commutative;
    }

    public void setCommutative(boolean commutative) {
        this.commutative = commutative;
    }
    public String getExecutiontime() {
        return executionTime;
    }

    public void setExecutiontime(String executionTime) {
        this.executionTime = executionTime;
    }
    public String getWorkingpath() {
        return workingPath;
    }

    public void setWorkingpath(String workingPath) {
        this.workingPath = workingPath;
    }


}