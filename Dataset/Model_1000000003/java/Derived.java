





import java.util.List;
import java.util.ArrayList;

public class Derived extends Metric {

    private String expression;



    public Derived(
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