





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_statements_AssignmentStmt extends Statement {

    private String operator;





    private kernel_Expression kernel_expression;




    private kernel_Expression kernel_expression;


    public ClockRDL_statements_AssignmentStmt(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public kernel_Expression getKernel_expression() {
        return kernel_expression;
    }

    public void setKernel_expression(kernel_Expression kernel_expression) {
        this.kernel_expression = kernel_expression;
    }
    public kernel_Expression getKernel_expression() {
        return kernel_expression;
    }

    public void setKernel_expression(kernel_Expression kernel_expression) {
        this.kernel_expression = kernel_expression;
    }

}