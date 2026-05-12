





import java.util.List;
import java.util.ArrayList;

public class jpql_AndExpression extends Expression {






    private List<jpql_Expression> jpql_expressions;


    public jpql_AndExpression(
    ) {
        super(
        );
        this.jpql_expressions = new ArrayList<>();
    }

    public jpql_AndExpression(
        ArrayList<jpql_Expression> jpql_expressions    ) {
        this.jpql_expressions = jpql_expressions;
    }


    public List<jpql_Expression> getJpql_expressions() {
        return jpql_expressions;
    }

    public void addJpql_expression(Jpql_expression jpql_expression) {
        this.jpql_expressions.add(jpql_expression);
    }

}