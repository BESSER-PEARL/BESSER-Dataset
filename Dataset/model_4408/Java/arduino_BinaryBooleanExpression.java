





import java.util.List;
import java.util.ArrayList;

public class arduino_BinaryBooleanExpression extends BinaryExpression, BooleanExpression {

    private String operator;



    public arduino_BinaryBooleanExpression(
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