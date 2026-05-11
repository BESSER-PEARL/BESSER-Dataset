





import java.util.List;
import java.util.ArrayList;

public class flowchartpck_RelationalExpression extends Expression {

    private String operator;



    public flowchartpck_RelationalExpression(
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