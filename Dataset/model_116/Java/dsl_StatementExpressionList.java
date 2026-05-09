





import java.util.List;
import java.util.ArrayList;

public class dsl_StatementExpressionList  {






    private List<dsl_StatementExpression> dsl_statementexpressions;




    private dsl_ForUpdate dsl_forupdate;




    private dsl_ForInit dsl_forinit;


    public dsl_StatementExpressionList(
    ) {
        this.dsl_statementexpressions = new ArrayList<>();
    }

    public dsl_StatementExpressionList(
        ArrayList<dsl_StatementExpression> dsl_statementexpressions    ) {
        this.dsl_statementexpressions = dsl_statementexpressions;
    }


    public List<dsl_StatementExpression> getDsl_statementexpressions() {
        return dsl_statementexpressions;
    }

    public void addDsl_statementexpression(Dsl_statementexpression dsl_statementexpression) {
        this.dsl_statementexpressions.add(dsl_statementexpression);
    }
    public dsl_ForUpdate getDsl_forupdate() {
        return dsl_forupdate;
    }

    public void setDsl_forupdate(dsl_ForUpdate dsl_forupdate) {
        this.dsl_forupdate = dsl_forupdate;
    }
    public dsl_ForInit getDsl_forinit() {
        return dsl_forinit;
    }

    public void setDsl_forinit(dsl_ForInit dsl_forinit) {
        this.dsl_forinit = dsl_forinit;
    }

}