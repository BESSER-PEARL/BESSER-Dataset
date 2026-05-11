





import java.util.List;
import java.util.ArrayList;

public class swrtj_BooleanOperator  {

    private String operator;





    private swrtj_BooleanExpression swrtj_booleanexpression;


    public swrtj_BooleanOperator(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public swrtj_BooleanExpression getSwrtj_booleanexpression() {
        return swrtj_booleanexpression;
    }

    public void setSwrtj_booleanexpression(swrtj_BooleanExpression swrtj_booleanexpression) {
        this.swrtj_booleanexpression = swrtj_booleanexpression;
    }

}