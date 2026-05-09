





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_WhileStatement extends IterationStatement {






    private Expression expression;




    private EmbeddedStatement embeddedstatement;


    public c_sharp_statements_WhileStatement(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public EmbeddedStatement getEmbeddedstatement() {
        return embeddedstatement;
    }

    public void setEmbeddedstatement(EmbeddedStatement embeddedstatement) {
        this.embeddedstatement = embeddedstatement;
    }

}