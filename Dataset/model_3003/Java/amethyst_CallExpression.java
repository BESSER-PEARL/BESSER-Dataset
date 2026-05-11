





import java.util.List;
import java.util.ArrayList;

public class amethyst_CallExpression extends Expression {






    private List<amethyst_Expression> amethyst_expressions;




    private amethyst_Expression amethyst_expression;


    public amethyst_CallExpression(
    ) {
        super(
        );
        this.amethyst_expressions = new ArrayList<>();
    }

    public amethyst_CallExpression(
        ArrayList<amethyst_Expression> amethyst_expressions    ) {
        this.amethyst_expressions = amethyst_expressions;
    }


    public List<amethyst_Expression> getAmethyst_expressions() {
        return amethyst_expressions;
    }

    public void addAmethyst_expression(Amethyst_expression amethyst_expression) {
        this.amethyst_expressions.add(amethyst_expression);
    }
    public amethyst_Expression getAmethyst_expression() {
        return amethyst_expression;
    }

    public void setAmethyst_expression(amethyst_Expression amethyst_expression) {
        this.amethyst_expression = amethyst_expression;
    }

}