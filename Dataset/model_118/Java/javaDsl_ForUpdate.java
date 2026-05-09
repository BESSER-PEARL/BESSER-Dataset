





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ForUpdate  {






    private List<javaDsl_StatementExpression> javadsl_statementexpressions;




    private javaDsl_ForStatement javadsl_forstatement;


    public javaDsl_ForUpdate(
    ) {
        this.javadsl_statementexpressions = new ArrayList<>();
    }

    public javaDsl_ForUpdate(
        ArrayList<javaDsl_StatementExpression> javadsl_statementexpressions    ) {
        this.javadsl_statementexpressions = javadsl_statementexpressions;
    }


    public List<javaDsl_StatementExpression> getJavadsl_statementexpressions() {
        return javadsl_statementexpressions;
    }

    public void addJavadsl_statementexpression(Javadsl_statementexpression javadsl_statementexpression) {
        this.javadsl_statementexpressions.add(javadsl_statementexpression);
    }
    public javaDsl_ForStatement getJavadsl_forstatement() {
        return javadsl_forstatement;
    }

    public void setJavadsl_forstatement(javaDsl_ForStatement javadsl_forstatement) {
        this.javadsl_forstatement = javadsl_forstatement;
    }

}