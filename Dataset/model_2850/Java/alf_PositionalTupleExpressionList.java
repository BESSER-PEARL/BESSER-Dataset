





import java.util.List;
import java.util.ArrayList;

public class alf_PositionalTupleExpressionList  {






    private List<alf_Expression> alf_expressions;




    private alf_Tuple alf_tuple;


    public alf_PositionalTupleExpressionList(
    ) {
        this.alf_expressions = new ArrayList<>();
    }

    public alf_PositionalTupleExpressionList(
        ArrayList<alf_Expression> alf_expressions    ) {
        this.alf_expressions = alf_expressions;
    }


    public List<alf_Expression> getAlf_expressions() {
        return alf_expressions;
    }

    public void addAlf_expression(Alf_expression alf_expression) {
        this.alf_expressions.add(alf_expression);
    }
    public alf_Tuple getAlf_tuple() {
        return alf_tuple;
    }

    public void setAlf_tuple(alf_Tuple alf_tuple) {
        this.alf_tuple = alf_tuple;
    }

}