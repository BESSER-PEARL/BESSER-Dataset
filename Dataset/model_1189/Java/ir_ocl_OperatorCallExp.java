





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_OperatorCallExp extends CallExp {

    private String operator;





    private OclExpression oclexpression;


    public ir_ocl_OperatorCallExp(
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

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}