





import java.util.List;
import java.util.ArrayList;

public class CursorDeclaration  {






    private plsql_statement_OpenStatement plsql_statement_openstatement;




    private plsql_statement_CloseStatement plsql_statement_closestatement;




    private plsql_statement_FetchStatement plsql_statement_fetchstatement;




    private plsql_expression_FoundExpression plsql_expression_foundexpression;


    public CursorDeclaration(
    ) {
    }



    public plsql_statement_OpenStatement getPlsql_statement_openstatement() {
        return plsql_statement_openstatement;
    }

    public void setPlsql_statement_openstatement(plsql_statement_OpenStatement plsql_statement_openstatement) {
        this.plsql_statement_openstatement = plsql_statement_openstatement;
    }
    public plsql_statement_CloseStatement getPlsql_statement_closestatement() {
        return plsql_statement_closestatement;
    }

    public void setPlsql_statement_closestatement(plsql_statement_CloseStatement plsql_statement_closestatement) {
        this.plsql_statement_closestatement = plsql_statement_closestatement;
    }
    public plsql_statement_FetchStatement getPlsql_statement_fetchstatement() {
        return plsql_statement_fetchstatement;
    }

    public void setPlsql_statement_fetchstatement(plsql_statement_FetchStatement plsql_statement_fetchstatement) {
        this.plsql_statement_fetchstatement = plsql_statement_fetchstatement;
    }
    public plsql_expression_FoundExpression getPlsql_expression_foundexpression() {
        return plsql_expression_foundexpression;
    }

    public void setPlsql_expression_foundexpression(plsql_expression_FoundExpression plsql_expression_foundexpression) {
        this.plsql_expression_foundexpression = plsql_expression_foundexpression;
    }

}