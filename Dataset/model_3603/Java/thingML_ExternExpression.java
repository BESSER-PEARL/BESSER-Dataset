





import java.util.List;
import java.util.ArrayList;

public class thingML_ExternExpression extends Expression {

    private String expression;





    private List<thingML_Expression> thingml_expressions;


    public thingML_ExternExpression(
        String expression    ) {
        super(
        );
        this.expression = expression;
        this.thingml_expressions = new ArrayList<>();
    }

    public thingML_ExternExpression(
        String expression        ArrayList<thingML_Expression> thingml_expressions    ) {
        this.expression = expression;
        this.thingml_expressions = thingml_expressions;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public List<thingML_Expression> getThingml_expressions() {
        return thingml_expressions;
    }

    public void addThingml_expression(Thingml_expression thingml_expression) {
        this.thingml_expressions.add(thingml_expression);
    }

}