





import java.util.List;
import java.util.ArrayList;

public class fmpl_Relational extends Expression {

    private String operator;





    private fmpl_Cond fmpl_cond;




    private fmpl_Expression fmpl_expression;




    private fmpl_Expression fmpl_expression;


    public fmpl_Relational(
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

    public fmpl_Cond getFmpl_cond() {
        return fmpl_cond;
    }

    public void setFmpl_cond(fmpl_Cond fmpl_cond) {
        this.fmpl_cond = fmpl_cond;
    }
    public fmpl_Expression getFmpl_expression() {
        return fmpl_expression;
    }

    public void setFmpl_expression(fmpl_Expression fmpl_expression) {
        this.fmpl_expression = fmpl_expression;
    }
    public fmpl_Expression getFmpl_expression() {
        return fmpl_expression;
    }

    public void setFmpl_expression(fmpl_Expression fmpl_expression) {
        this.fmpl_expression = fmpl_expression;
    }

}