





import java.util.List;
import java.util.ArrayList;

public class amethyst_NewExpression extends Expression {






    private amethyst_ClassType amethyst_classtype;




    private List<amethyst_Expression> amethyst_expressions;


    public amethyst_NewExpression(
    ) {
        super(
        );
        this.amethyst_expressions = new ArrayList<>();
    }

    public amethyst_NewExpression(
        ArrayList<amethyst_Expression> amethyst_expressions    ) {
        this.amethyst_expressions = amethyst_expressions;
    }


    public amethyst_ClassType getAmethyst_classtype() {
        return amethyst_classtype;
    }

    public void setAmethyst_classtype(amethyst_ClassType amethyst_classtype) {
        this.amethyst_classtype = amethyst_classtype;
    }
    public List<amethyst_Expression> getAmethyst_expressions() {
        return amethyst_expressions;
    }

    public void addAmethyst_expression(Amethyst_expression amethyst_expression) {
        this.amethyst_expressions.add(amethyst_expression);
    }

}