





import java.util.List;
import java.util.ArrayList;

public class NQC_AssignmentStatement extends Statement {

    private String Operator;



    public NQC_AssignmentStatement(
        String Operator    ) {
        super(
        );
        this.Operator = Operator;
    }


    public String getOperator() {
        return Operator;
    }

    public void setOperator(String Operator) {
        this.Operator = Operator;
    }


}