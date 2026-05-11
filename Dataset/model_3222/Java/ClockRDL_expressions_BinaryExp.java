





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_expressions_BinaryExp extends Expression {

    private String operator;



    public ClockRDL_expressions_BinaryExp(
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