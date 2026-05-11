





import java.util.List;
import java.util.ArrayList;

public class uppaal_system_TemplateDeclaration extends Declaration {






    private List<Expression> expressions;


    public uppaal_system_TemplateDeclaration(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public uppaal_system_TemplateDeclaration(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}