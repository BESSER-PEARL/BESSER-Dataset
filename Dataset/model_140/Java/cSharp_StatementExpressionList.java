





import java.util.List;
import java.util.ArrayList;

public class cSharp_StatementExpressionList  {






    private List<cSharp_StatementExpression> csharp_statementexpressions;




    private cSharp_StatementExpression csharp_statementexpression;




    private cSharp_ForStatement csharp_forstatement;




    private cSharp_ForInitializer csharp_forinitializer;


    public cSharp_StatementExpressionList(
    ) {
        this.csharp_statementexpressions = new ArrayList<>();
    }

    public cSharp_StatementExpressionList(
        ArrayList<cSharp_StatementExpression> csharp_statementexpressions    ) {
        this.csharp_statementexpressions = csharp_statementexpressions;
    }


    public List<cSharp_StatementExpression> getCsharp_statementexpressions() {
        return csharp_statementexpressions;
    }

    public void addCsharp_statementexpression(Csharp_statementexpression csharp_statementexpression) {
        this.csharp_statementexpressions.add(csharp_statementexpression);
    }
    public cSharp_StatementExpression getCsharp_statementexpression() {
        return csharp_statementexpression;
    }

    public void setCsharp_statementexpression(cSharp_StatementExpression csharp_statementexpression) {
        this.csharp_statementexpression = csharp_statementexpression;
    }
    public cSharp_ForStatement getCsharp_forstatement() {
        return csharp_forstatement;
    }

    public void setCsharp_forstatement(cSharp_ForStatement csharp_forstatement) {
        this.csharp_forstatement = csharp_forstatement;
    }
    public cSharp_ForInitializer getCsharp_forinitializer() {
        return csharp_forinitializer;
    }

    public void setCsharp_forinitializer(cSharp_ForInitializer csharp_forinitializer) {
        this.csharp_forinitializer = csharp_forinitializer;
    }

}