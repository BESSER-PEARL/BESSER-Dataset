





import java.util.List;
import java.util.ArrayList;

public class sparql_OrFilterExpression extends Expression {






    private List<sparql_Expression> sparql_expressions;


    public sparql_OrFilterExpression(
    ) {
        super(
        );
        this.sparql_expressions = new ArrayList<>();
    }

    public sparql_OrFilterExpression(
        ArrayList<sparql_Expression> sparql_expressions    ) {
        this.sparql_expressions = sparql_expressions;
    }


    public List<sparql_Expression> getSparql_expressions() {
        return sparql_expressions;
    }

    public void addSparql_expression(Sparql_expression sparql_expression) {
        this.sparql_expressions.add(sparql_expression);
    }

}