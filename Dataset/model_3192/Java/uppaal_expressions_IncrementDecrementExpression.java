





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_IncrementDecrementExpression extends Expression {

    private String operator;
    private String position;



    public uppaal_expressions_IncrementDecrementExpression(
        String operator,        String position    ) {
        super(
        );
        this.operator = operator;
        this.position = position;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}