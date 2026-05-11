





import java.util.List;
import java.util.ArrayList;

public class nabla_FunctionCall extends Expression {






    private nabla_Function nabla_function;




    private List<nabla_Expression> nabla_expressions;


    public nabla_FunctionCall(
    ) {
        super(
        );
        this.nabla_expressions = new ArrayList<>();
    }

    public nabla_FunctionCall(
        ArrayList<nabla_Expression> nabla_expressions    ) {
        this.nabla_expressions = nabla_expressions;
    }


    public nabla_Function getNabla_function() {
        return nabla_function;
    }

    public void setNabla_function(nabla_Function nabla_function) {
        this.nabla_function = nabla_function;
    }
    public List<nabla_Expression> getNabla_expressions() {
        return nabla_expressions;
    }

    public void addNabla_expression(Nabla_expression nabla_expression) {
        this.nabla_expressions.add(nabla_expression);
    }

}