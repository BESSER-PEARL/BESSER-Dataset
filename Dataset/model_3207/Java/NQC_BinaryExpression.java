





import java.util.List;
import java.util.ArrayList;

public class NQC_BinaryExpression extends CompoundExpression {

    private String Operator;





    private NQC_Expression nqc_expression;




    private NQC_Expression nqc_expression;


    public NQC_BinaryExpression(
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

    public NQC_Expression getNqc_expression() {
        return nqc_expression;
    }

    public void setNqc_expression(NQC_Expression nqc_expression) {
        this.nqc_expression = nqc_expression;
    }
    public NQC_Expression getNqc_expression() {
        return nqc_expression;
    }

    public void setNqc_expression(NQC_Expression nqc_expression) {
        this.nqc_expression = nqc_expression;
    }

}