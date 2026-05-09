





import java.util.List;
import java.util.ArrayList;

public class model_values_Expression extends Value {

    private String expression;



    public model_values_Expression(
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