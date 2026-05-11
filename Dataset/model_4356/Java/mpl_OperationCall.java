





import java.util.List;
import java.util.ArrayList;

public class mpl_OperationCall extends AtomicExpression {






    private List<mpl_Expression> mpl_expressions;


    public mpl_OperationCall(
    ) {
        super(
        );
        this.mpl_expressions = new ArrayList<>();
    }

    public mpl_OperationCall(
        ArrayList<mpl_Expression> mpl_expressions    ) {
        this.mpl_expressions = mpl_expressions;
    }


    public List<mpl_Expression> getMpl_expressions() {
        return mpl_expressions;
    }

    public void addMpl_expression(Mpl_expression mpl_expression) {
        this.mpl_expressions.add(mpl_expression);
    }

}