





import java.util.List;
import java.util.ArrayList;

public class SQLDML_FunctionExp extends Predicate {

    private String name;





    private List<Expression> expressions;


    public SQLDML_FunctionExp(
        String name    ) {
        super(
        );
        this.name = name;
        this.expressions = new ArrayList<>();
    }

    public SQLDML_FunctionExp(
        String name        ArrayList<Expression> expressions    ) {
        this.name = name;
        this.expressions = expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}