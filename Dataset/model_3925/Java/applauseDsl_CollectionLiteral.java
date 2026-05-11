





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_CollectionLiteral extends Expression, CollectionExpression {






    private List<applauseDsl_ScalarExpression> applausedsl_scalarexpressions;


    public applauseDsl_CollectionLiteral(
    ) {
        super(
        );
        this.applausedsl_scalarexpressions = new ArrayList<>();
    }

    public applauseDsl_CollectionLiteral(
        ArrayList<applauseDsl_ScalarExpression> applausedsl_scalarexpressions    ) {
        this.applausedsl_scalarexpressions = applausedsl_scalarexpressions;
    }


    public List<applauseDsl_ScalarExpression> getApplausedsl_scalarexpressions() {
        return applausedsl_scalarexpressions;
    }

    public void addApplausedsl_scalarexpression(Applausedsl_scalarexpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpressions.add(applausedsl_scalarexpression);
    }

}