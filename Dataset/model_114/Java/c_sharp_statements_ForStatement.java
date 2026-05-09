





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_ForStatement extends IterationStatement {






    private EmbeddedStatement embeddedstatement;




    private Expression expression;


    public c_sharp_statements_ForStatement(
    ) {
        super(
        );
    }



    public EmbeddedStatement getEmbeddedstatement() {
        return embeddedstatement;
    }

    public void setEmbeddedstatement(EmbeddedStatement embeddedstatement) {
        this.embeddedstatement = embeddedstatement;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}