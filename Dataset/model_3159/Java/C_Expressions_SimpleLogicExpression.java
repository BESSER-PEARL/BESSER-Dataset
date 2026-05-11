





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_SimpleLogicExpression extends LogicExpression {

    private String operator;



    public C_Expressions_SimpleLogicExpression(
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


}