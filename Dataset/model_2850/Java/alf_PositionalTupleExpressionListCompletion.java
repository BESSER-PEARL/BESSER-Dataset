





import java.util.List;
import java.util.ArrayList;

public class alf_PositionalTupleExpressionListCompletion  {






    private List<alf_Expression> alf_expressions;


    public alf_PositionalTupleExpressionListCompletion(
    ) {
        this.alf_expressions = new ArrayList<>();
    }

    public alf_PositionalTupleExpressionListCompletion(
        ArrayList<alf_Expression> alf_expressions    ) {
        this.alf_expressions = alf_expressions;
    }


    public List<alf_Expression> getAlf_expressions() {
        return alf_expressions;
    }

    public void addAlf_expression(Alf_expression alf_expression) {
        this.alf_expressions.add(alf_expression);
    }

}