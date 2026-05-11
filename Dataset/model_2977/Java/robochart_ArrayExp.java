





import java.util.List;
import java.util.ArrayList;

public class robochart_ArrayExp extends Expression {






    private List<robochart_Expression> robochart_expressions;




    private robochart_Expression robochart_expression;


    public robochart_ArrayExp(
    ) {
        super(
        );
        this.robochart_expressions = new ArrayList<>();
    }

    public robochart_ArrayExp(
        ArrayList<robochart_Expression> robochart_expressions    ) {
        this.robochart_expressions = robochart_expressions;
    }


    public List<robochart_Expression> getRobochart_expressions() {
        return robochart_expressions;
    }

    public void addRobochart_expression(Robochart_expression robochart_expression) {
        this.robochart_expressions.add(robochart_expression);
    }
    public robochart_Expression getRobochart_expression() {
        return robochart_expression;
    }

    public void setRobochart_expression(robochart_Expression robochart_expression) {
        this.robochart_expression = robochart_expression;
    }

}