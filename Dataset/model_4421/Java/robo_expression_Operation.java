





import java.util.List;
import java.util.ArrayList;

public class robo_expression_Operation extends Expr {

    private String operator;



    public robo_expression_Operation(
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