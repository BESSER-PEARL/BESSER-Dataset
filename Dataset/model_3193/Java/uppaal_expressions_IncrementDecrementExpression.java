





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_IncrementDecrementExpression extends Expression {

    private String position;
    private String operator;



    public uppaal_expressions_IncrementDecrementExpression(
        String position,        String operator    ) {
        super(
        );
        this.position = position;
        this.operator = operator;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}