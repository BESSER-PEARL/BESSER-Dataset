





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Guards extends Position {






    private List<expressions_Expression> expressions_expressions;


    public timedAutomata_core_Guards(
    ) {
        super(
        );
        this.expressions_expressions = new ArrayList<>();
    }

    public timedAutomata_core_Guards(
        ArrayList<expressions_Expression> expressions_expressions    ) {
        this.expressions_expressions = expressions_expressions;
    }


    public List<expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }

}