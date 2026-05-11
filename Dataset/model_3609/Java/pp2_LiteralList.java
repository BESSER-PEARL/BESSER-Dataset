





import java.util.List;
import java.util.ArrayList;

public class pp2_LiteralList extends LiteralExpression {






    private List<pp2_Expression> pp2_expressions;


    public pp2_LiteralList(
    ) {
        super(
        );
        this.pp2_expressions = new ArrayList<>();
    }

    public pp2_LiteralList(
        ArrayList<pp2_Expression> pp2_expressions    ) {
        this.pp2_expressions = pp2_expressions;
    }


    public List<pp2_Expression> getPp2_expressions() {
        return pp2_expressions;
    }

    public void addPp2_expression(Pp2_expression pp2_expression) {
        this.pp2_expressions.add(pp2_expression);
    }

}