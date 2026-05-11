





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_OneOperator extends Expression {

    private String operator;





    private dinkiemodel_Expression dinkiemodel_expression;


    public dinkiemodel_OneOperator(
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

    public dinkiemodel_Expression getDinkiemodel_expression() {
        return dinkiemodel_expression;
    }

    public void setDinkiemodel_expression(dinkiemodel_Expression dinkiemodel_expression) {
        this.dinkiemodel_expression = dinkiemodel_expression;
    }

}