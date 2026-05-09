





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_ForeachStatement extends IterationStatement {






    private Expression expression;




    private Identifier identifier;




    private EmbeddedStatement embeddedstatement;




    private Type type;


    public c_sharp_statements_ForeachStatement(
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
    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public EmbeddedStatement getEmbeddedstatement() {
        return embeddedstatement;
    }

    public void setEmbeddedstatement(EmbeddedStatement embeddedstatement) {
        this.embeddedstatement = embeddedstatement;
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}