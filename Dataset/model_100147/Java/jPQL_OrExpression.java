





import java.util.List;
import java.util.ArrayList;

public class jPQL_OrExpression extends Expression {






    private List<jPQL_Expression> jpql_expressions;


    public jPQL_OrExpression(
    ) {
        super(
        );
        this.jpql_expressions = new ArrayList<>();
    }

    public jPQL_OrExpression(
        ArrayList<jPQL_Expression> jpql_expressions    ) {
        this.jpql_expressions = jpql_expressions;
    }


    public List<jPQL_Expression> getJpql_expressions() {
        return jpql_expressions;
    }

    public void addJpql_expression(Jpql_expression jpql_expression) {
        this.jpql_expressions.add(jpql_expression);
    }

}