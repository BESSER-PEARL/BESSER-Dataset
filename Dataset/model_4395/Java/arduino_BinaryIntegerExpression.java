





import java.util.List;
import java.util.ArrayList;

public class arduino_BinaryIntegerExpression extends BinaryExpression, IntegerExpression {

    private String operator;



    public arduino_BinaryIntegerExpression(
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