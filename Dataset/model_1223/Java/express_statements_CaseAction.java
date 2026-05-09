





import java.util.List;
import java.util.ArrayList;

public class express_statements_CaseAction  {

    private String isDefault;





    private List<Expression> expressions;




    private Statement statement;


    public express_statements_CaseAction(
        String isDefault    ) {
        this.isDefault = isDefault;
        this.expressions = new ArrayList<>();
    }

    public express_statements_CaseAction(
        String isDefault        ArrayList<Expression> expressions    ) {
        this.isDefault = isDefault;
        this.expressions = expressions;
    }

    public String getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(String isDefault) {
        this.isDefault = isDefault;
    }

    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }
    public Statement getStatement() {
        return statement;
    }

    public void setStatement(Statement statement) {
        this.statement = statement;
    }

}