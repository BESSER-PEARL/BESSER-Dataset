





import java.util.List;
import java.util.ArrayList;

public class java_Assignment extends Expression {

    private String operator;



    public java_Assignment(
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