





import java.util.List;
import java.util.ArrayList;

public class mql_OrExpression extends Expression {






    private List<mql_Expression> mql_expressions;


    public mql_OrExpression(
    ) {
        super(
        );
        this.mql_expressions = new ArrayList<>();
    }

    public mql_OrExpression(
        ArrayList<mql_Expression> mql_expressions    ) {
        this.mql_expressions = mql_expressions;
    }


    public List<mql_Expression> getMql_expressions() {
        return mql_expressions;
    }

    public void addMql_expression(Mql_expression mql_expression) {
        this.mql_expressions.add(mql_expression);
    }

}