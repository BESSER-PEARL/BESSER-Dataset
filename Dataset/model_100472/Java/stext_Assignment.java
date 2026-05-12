





import java.util.List;
import java.util.ArrayList;

public class stext_Assignment extends Statement {

    private String operator;



    public stext_Assignment(
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