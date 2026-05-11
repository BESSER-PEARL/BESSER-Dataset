





import java.util.List;
import java.util.ArrayList;

public class arduino_MathOperator extends Value, Instruction {

    private String operator;



    public arduino_MathOperator(
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