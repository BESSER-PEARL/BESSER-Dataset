





import java.util.List;
import java.util.ArrayList;

public class miniJava_FunctionCall extends AbstractExpression {






    private miniJava_AbstractExpression minijava_abstractexpression;




    private miniJava_Identifier minijava_identifier;




    private List<miniJava_AbstractExpression> minijava_abstractexpressions;


    public miniJava_FunctionCall(
    ) {
        super(
        );
        this.minijava_abstractexpressions = new ArrayList<>();
    }

    public miniJava_FunctionCall(
        ArrayList<miniJava_AbstractExpression> minijava_abstractexpressions    ) {
        this.minijava_abstractexpressions = minijava_abstractexpressions;
    }


    public miniJava_AbstractExpression getMinijava_abstractexpression() {
        return minijava_abstractexpression;
    }

    public void setMinijava_abstractexpression(miniJava_AbstractExpression minijava_abstractexpression) {
        this.minijava_abstractexpression = minijava_abstractexpression;
    }
    public miniJava_Identifier getMinijava_identifier() {
        return minijava_identifier;
    }

    public void setMinijava_identifier(miniJava_Identifier minijava_identifier) {
        this.minijava_identifier = minijava_identifier;
    }
    public List<miniJava_AbstractExpression> getMinijava_abstractexpressions() {
        return minijava_abstractexpressions;
    }

    public void addMinijava_abstractexpression(Minijava_abstractexpression minijava_abstractexpression) {
        this.minijava_abstractexpressions.add(minijava_abstractexpression);
    }

}