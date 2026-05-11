





import java.util.List;
import java.util.ArrayList;

public class arithmetics_FunctionCall extends Expression {






    private List<arithmetics_Expression> arithmetics_expressions;




    private arithmetics_AbstractDefinition arithmetics_abstractdefinition;


    public arithmetics_FunctionCall(
    ) {
        super(
        );
        this.arithmetics_expressions = new ArrayList<>();
    }

    public arithmetics_FunctionCall(
        ArrayList<arithmetics_Expression> arithmetics_expressions    ) {
        this.arithmetics_expressions = arithmetics_expressions;
    }


    public List<arithmetics_Expression> getArithmetics_expressions() {
        return arithmetics_expressions;
    }

    public void addArithmetics_expression(Arithmetics_expression arithmetics_expression) {
        this.arithmetics_expressions.add(arithmetics_expression);
    }
    public arithmetics_AbstractDefinition getArithmetics_abstractdefinition() {
        return arithmetics_abstractdefinition;
    }

    public void setArithmetics_abstractdefinition(arithmetics_AbstractDefinition arithmetics_abstractdefinition) {
        this.arithmetics_abstractdefinition = arithmetics_abstractdefinition;
    }

}