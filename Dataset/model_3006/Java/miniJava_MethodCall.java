





import java.util.List;
import java.util.ArrayList;

public class miniJava_MethodCall extends Expression {






    private miniJava_Expression minijava_expression;




    private miniJava_Method minijava_method;




    private List<miniJava_Expression> minijava_expressions;


    public miniJava_MethodCall(
    ) {
        super(
        );
        this.minijava_expressions = new ArrayList<>();
    }

    public miniJava_MethodCall(
        ArrayList<miniJava_Expression> minijava_expressions    ) {
        this.minijava_expressions = minijava_expressions;
    }


    public miniJava_Expression getMinijava_expression() {
        return minijava_expression;
    }

    public void setMinijava_expression(miniJava_Expression minijava_expression) {
        this.minijava_expression = minijava_expression;
    }
    public miniJava_Method getMinijava_method() {
        return minijava_method;
    }

    public void setMinijava_method(miniJava_Method minijava_method) {
        this.minijava_method = minijava_method;
    }
    public List<miniJava_Expression> getMinijava_expressions() {
        return minijava_expressions;
    }

    public void addMinijava_expression(Minijava_expression minijava_expression) {
        this.minijava_expressions.add(minijava_expression);
    }

}