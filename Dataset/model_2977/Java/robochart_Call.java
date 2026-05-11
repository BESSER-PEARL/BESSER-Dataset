





import java.util.List;
import java.util.ArrayList;

public class robochart_Call extends Statement {






    private robochart_OperationSig robochart_operationsig;




    private List<robochart_Expression> robochart_expressions;


    public robochart_Call(
    ) {
        super(
        );
        this.robochart_expressions = new ArrayList<>();
    }

    public robochart_Call(
        ArrayList<robochart_Expression> robochart_expressions    ) {
        this.robochart_expressions = robochart_expressions;
    }


    public robochart_OperationSig getRobochart_operationsig() {
        return robochart_operationsig;
    }

    public void setRobochart_operationsig(robochart_OperationSig robochart_operationsig) {
        this.robochart_operationsig = robochart_operationsig;
    }
    public List<robochart_Expression> getRobochart_expressions() {
        return robochart_expressions;
    }

    public void addRobochart_expression(Robochart_expression robochart_expression) {
        this.robochart_expressions.add(robochart_expression);
    }

}