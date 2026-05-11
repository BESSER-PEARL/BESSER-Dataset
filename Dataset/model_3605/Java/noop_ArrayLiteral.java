





import java.util.List;
import java.util.ArrayList;

public class noop_ArrayLiteral extends Expression {






    private List<noop_Expression> noop_expressions;


    public noop_ArrayLiteral(
    ) {
        super(
        );
        this.noop_expressions = new ArrayList<>();
    }

    public noop_ArrayLiteral(
        ArrayList<noop_Expression> noop_expressions    ) {
        this.noop_expressions = noop_expressions;
    }


    public List<noop_Expression> getNoop_expressions() {
        return noop_expressions;
    }

    public void addNoop_expression(Noop_expression noop_expression) {
        this.noop_expressions.add(noop_expression);
    }

}