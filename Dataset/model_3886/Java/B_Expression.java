





import java.util.List;
import java.util.ArrayList;

public class B_Expression  {

    private String expression;





    private B_Operation b_operation;




    private B_Any b_any;


    public B_Expression(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public B_Operation getB_operation() {
        return b_operation;
    }

    public void setB_operation(B_Operation b_operation) {
        this.b_operation = b_operation;
    }
    public B_Any getB_any() {
        return b_any;
    }

    public void setB_any(B_Any b_any) {
        this.b_any = b_any;
    }

}