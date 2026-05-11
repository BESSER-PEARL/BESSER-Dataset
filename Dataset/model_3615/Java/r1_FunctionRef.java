





import java.util.List;
import java.util.ArrayList;

public class r1_FunctionRef extends ExpressionRef {






    private List<r1_Expression> r1_expressions;


    public r1_FunctionRef(
    ) {
        super(
        );
        this.r1_expressions = new ArrayList<>();
    }

    public r1_FunctionRef(
        ArrayList<r1_Expression> r1_expressions    ) {
        this.r1_expressions = r1_expressions;
    }


    public List<r1_Expression> getR1_expressions() {
        return r1_expressions;
    }

    public void addR1_expression(R1_expression r1_expression) {
        this.r1_expressions.add(r1_expression);
    }

}