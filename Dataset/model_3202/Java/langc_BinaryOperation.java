





import java.util.List;
import java.util.ArrayList;

public class langc_BinaryOperation extends Expression {

    private String operator;



    public langc_BinaryOperation(
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