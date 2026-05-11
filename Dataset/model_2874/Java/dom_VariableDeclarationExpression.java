





import java.util.List;
import java.util.ArrayList;

public class dom_VariableDeclarationExpression extends Expression {






    private List<dom_Expression> dom_expressions;




    private dom_NameExpression dom_nameexpression;


    public dom_VariableDeclarationExpression(
    ) {
        super(
        );
        this.dom_expressions = new ArrayList<>();
    }

    public dom_VariableDeclarationExpression(
        ArrayList<dom_Expression> dom_expressions    ) {
        this.dom_expressions = dom_expressions;
    }


    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }
    public dom_NameExpression getDom_nameexpression() {
        return dom_nameexpression;
    }

    public void setDom_nameexpression(dom_NameExpression dom_nameexpression) {
        this.dom_nameexpression = dom_nameexpression;
    }

}