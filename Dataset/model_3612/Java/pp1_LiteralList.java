





import java.util.List;
import java.util.ArrayList;

public class pp1_LiteralList extends LiteralExpression {






    private List<pp1_Expression> pp1_expressions;


    public pp1_LiteralList(
    ) {
        super(
        );
        this.pp1_expressions = new ArrayList<>();
    }

    public pp1_LiteralList(
        ArrayList<pp1_Expression> pp1_expressions    ) {
        this.pp1_expressions = pp1_expressions;
    }


    public List<pp1_Expression> getPp1_expressions() {
        return pp1_expressions;
    }

    public void addPp1_expression(Pp1_expression pp1_expression) {
        this.pp1_expressions.add(pp1_expression);
    }

}