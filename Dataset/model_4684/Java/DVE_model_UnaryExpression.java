





import java.util.List;
import java.util.ArrayList;

public class DVE_model_UnaryExpression extends Expression {

    private String operator;



    public DVE_model_UnaryExpression(
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