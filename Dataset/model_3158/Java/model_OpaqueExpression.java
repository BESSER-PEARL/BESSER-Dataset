





import java.util.List;
import java.util.ArrayList;

public class model_OpaqueExpression extends NullaryExpression {

    private String expression;



    public model_OpaqueExpression(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}