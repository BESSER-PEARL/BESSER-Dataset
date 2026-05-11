





import java.util.List;
import java.util.ArrayList;

public class miniJava_NumberValue  {

    private int value;





    private miniJava_Expr minijava_expr;


    public miniJava_NumberValue(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public miniJava_Expr getMinijava_expr() {
        return minijava_expr;
    }

    public void setMinijava_expr(miniJava_Expr minijava_expr) {
        this.minijava_expr = minijava_expr;
    }

}