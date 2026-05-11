





import java.util.List;
import java.util.ArrayList;

public class frontend_qool_EmitStatement extends Statement {






    private QoolQueue qoolqueue;




    private Expression expression;


    public frontend_qool_EmitStatement(
    ) {
        super(
        );
    }



    public QoolQueue getQoolqueue() {
        return qoolqueue;
    }

    public void setQoolqueue(QoolQueue qoolqueue) {
        this.qoolqueue = qoolqueue;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}