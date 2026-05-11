





import java.util.List;
import java.util.ArrayList;

public class simple_csp_SetOp extends Operator {






    private List<simple_csp_Expression> simple_csp_expressions;


    public simple_csp_SetOp(
    ) {
        super(
        );
        this.simple_csp_expressions = new ArrayList<>();
    }

    public simple_csp_SetOp(
        ArrayList<simple_csp_Expression> simple_csp_expressions    ) {
        this.simple_csp_expressions = simple_csp_expressions;
    }


    public List<simple_csp_Expression> getSimple_csp_expressions() {
        return simple_csp_expressions;
    }

    public void addSimple_csp_expression(Simple_csp_expression simple_csp_expression) {
        this.simple_csp_expressions.add(simple_csp_expression);
    }

}