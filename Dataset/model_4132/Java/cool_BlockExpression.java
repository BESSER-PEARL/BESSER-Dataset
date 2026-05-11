





import java.util.List;
import java.util.ArrayList;

public class cool_BlockExpression extends PrimaryExpression {






    private List<cool_Expression> cool_expressions;


    public cool_BlockExpression(
    ) {
        super(
        );
        this.cool_expressions = new ArrayList<>();
    }

    public cool_BlockExpression(
        ArrayList<cool_Expression> cool_expressions    ) {
        this.cool_expressions = cool_expressions;
    }


    public List<cool_Expression> getCool_expressions() {
        return cool_expressions;
    }

    public void addCool_expression(Cool_expression cool_expression) {
        this.cool_expressions.add(cool_expression);
    }

}