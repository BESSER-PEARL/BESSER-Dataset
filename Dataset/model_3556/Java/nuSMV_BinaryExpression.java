





import java.util.List;
import java.util.ArrayList;

public class nuSMV_BinaryExpression extends SimpleExpression {

    private String operator;
    private String op;





    private nuSMV_SimpleExpression nusmv_simpleexpression;




    private nuSMV_SimpleExpression nusmv_simpleexpression;


    public nuSMV_BinaryExpression(
        String operator,        String op    ) {
        super(
        );
        this.operator = operator;
        this.op = op;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }
    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }

}