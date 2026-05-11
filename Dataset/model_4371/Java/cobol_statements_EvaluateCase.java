





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_EvaluateCase extends NestedStatement {






    private List<ExpressionList> expressionlists;


    public cobol_statements_EvaluateCase(
    ) {
        super(
        );
        this.expressionlists = new ArrayList<>();
    }

    public cobol_statements_EvaluateCase(
        ArrayList<ExpressionList> expressionlists    ) {
        this.expressionlists = expressionlists;
    }


    public List<ExpressionList> getExpressionlists() {
        return expressionlists;
    }

    public void addExpressionlist(Expressionlist expressionlist) {
        this.expressionlists.add(expressionlist);
    }

}