





import java.util.List;
import java.util.ArrayList;

public class Logo_BooleanExpr extends BinaryExpr {

    private String operator;



    public Logo_BooleanExpr(
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