





import java.util.List;
import java.util.ArrayList;

public class pp_LiteralList extends LiteralExpression {






    private List<pp_Expression> pp_expressions;


    public pp_LiteralList(
    ) {
        super(
        );
        this.pp_expressions = new ArrayList<>();
    }

    public pp_LiteralList(
        ArrayList<pp_Expression> pp_expressions    ) {
        this.pp_expressions = pp_expressions;
    }


    public List<pp_Expression> getPp_expressions() {
        return pp_expressions;
    }

    public void addPp_expression(Pp_expression pp_expression) {
        this.pp_expressions.add(pp_expression);
    }

}