





import java.util.List;
import java.util.ArrayList;

public class Statement  {






    private statements_Condition statements_condition;




    private statements_StatementListContainer statements_statementlistcontainer;




    private statements_StatementContainer statements_statementcontainer;


    public Statement(
    ) {
    }



    public statements_Condition getStatements_condition() {
        return statements_condition;
    }

    public void setStatements_condition(statements_Condition statements_condition) {
        this.statements_condition = statements_condition;
    }
    public statements_StatementListContainer getStatements_statementlistcontainer() {
        return statements_statementlistcontainer;
    }

    public void setStatements_statementlistcontainer(statements_StatementListContainer statements_statementlistcontainer) {
        this.statements_statementlistcontainer = statements_statementlistcontainer;
    }
    public statements_StatementContainer getStatements_statementcontainer() {
        return statements_statementcontainer;
    }

    public void setStatements_statementcontainer(statements_StatementContainer statements_statementcontainer) {
        this.statements_statementcontainer = statements_statementcontainer;
    }

}