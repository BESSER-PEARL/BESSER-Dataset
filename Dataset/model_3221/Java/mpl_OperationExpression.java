





import java.util.List;
import java.util.ArrayList;

public class mpl_OperationExpression extends Expression {






    private List<mpl_Expression> mpl_expressions;




    private mpl_Operation mpl_operation;


    public mpl_OperationExpression(
    ) {
        super(
        );
        this.mpl_expressions = new ArrayList<>();
    }

    public mpl_OperationExpression(
        ArrayList<mpl_Expression> mpl_expressions    ) {
        this.mpl_expressions = mpl_expressions;
    }


    public List<mpl_Expression> getMpl_expressions() {
        return mpl_expressions;
    }

    public void addMpl_expression(Mpl_expression mpl_expression) {
        this.mpl_expressions.add(mpl_expression);
    }
    public mpl_Operation getMpl_operation() {
        return mpl_operation;
    }

    public void setMpl_operation(mpl_Operation mpl_operation) {
        this.mpl_operation = mpl_operation;
    }

}