





import java.util.List;
import java.util.ArrayList;

public class B_Begin extends Expression {






    private List<B_Expression> b_expressions;


    public B_Begin(
    ) {
        super(
        );
        this.b_expressions = new ArrayList<>();
    }

    public B_Begin(
        ArrayList<B_Expression> b_expressions    ) {
        this.b_expressions = b_expressions;
    }


    public List<B_Expression> getB_expressions() {
        return b_expressions;
    }

    public void addB_expression(B_expression b_expression) {
        this.b_expressions.add(b_expression);
    }

}