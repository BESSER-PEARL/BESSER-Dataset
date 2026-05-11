





import java.util.List;
import java.util.ArrayList;

public class mid_operator_Operator extends GenericElement {

    private String executionTime;
    private boolean updateMID;
    private boolean commutative;
    private String inputSubdir;





    private Operator operator;


    public mid_operator_Operator(
        String executionTime,        boolean updateMID,        boolean commutative,        String inputSubdir    ) {
        super(
        );
        this.executionTime = executionTime;
        this.updateMID = updateMID;
        this.commutative = commutative;
        this.inputSubdir = inputSubdir;
    }


    public String getExecutiontime() {
        return executionTime;
    }

    public void setExecutiontime(String executionTime) {
        this.executionTime = executionTime;
    }
    public boolean getUpdatemid() {
        return updateMID;
    }

    public void setUpdatemid(boolean updateMID) {
        this.updateMID = updateMID;
    }
    public boolean getCommutative() {
        return commutative;
    }

    public void setCommutative(boolean commutative) {
        this.commutative = commutative;
    }
    public String getInputsubdir() {
        return inputSubdir;
    }

    public void setInputsubdir(String inputSubdir) {
        this.inputSubdir = inputSubdir;
    }

    public Operator getOperator() {
        return operator;
    }

    public void setOperator(Operator operator) {
        this.operator = operator;
    }

}