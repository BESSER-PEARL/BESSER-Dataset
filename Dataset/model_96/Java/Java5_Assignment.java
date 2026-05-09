





import java.util.List;
import java.util.ArrayList;

public class Java5_Assignment extends Expression {

    private String operator;



    public Java5_Assignment(
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