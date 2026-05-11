





import java.util.List;
import java.util.ArrayList;

public class prolog_List extends Term {






    private List<Expression> expressions;




    private List<Expression> expressions;


    public prolog_List(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
        this.expressions = new ArrayList<>();
    }

    public prolog_List(
        ArrayList<Expression> expressions,        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }
    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}