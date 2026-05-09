





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_IfStatement extends SelectionStatement {






    private List<EmbeddedStatement> embeddedstatements;




    private Expression expression;


    public c_sharp_statements_IfStatement(
    ) {
        super(
        );
        this.embeddedstatements = new ArrayList<>();
    }

    public c_sharp_statements_IfStatement(
        ArrayList<EmbeddedStatement> embeddedstatements    ) {
        this.embeddedstatements = embeddedstatements;
    }


    public List<EmbeddedStatement> getEmbeddedstatements() {
        return embeddedstatements;
    }

    public void addEmbeddedstatement(Embeddedstatement embeddedstatement) {
        this.embeddedstatements.add(embeddedstatement);
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}