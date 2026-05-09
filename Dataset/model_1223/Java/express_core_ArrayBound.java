





import java.util.List;
import java.util.ArrayList;

public class express_core_ArrayBound  {

    private String bound;





    private Expression expression;


    public express_core_ArrayBound(
        String bound    ) {
        this.bound = bound;
    }


    public String getBound() {
        return bound;
    }

    public void setBound(String bound) {
        this.bound = bound;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}