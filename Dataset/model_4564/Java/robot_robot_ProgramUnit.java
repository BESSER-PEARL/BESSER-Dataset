





import java.util.List;
import java.util.ArrayList;

public class robot_robot_ProgramUnit  {






    private List<Expression> expressions;


    public robot_robot_ProgramUnit(
    ) {
        this.expressions = new ArrayList<>();
    }

    public robot_robot_ProgramUnit(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}