





import java.util.List;
import java.util.ArrayList;

public class sql_OrExpr  {






    private sql_FromTableJoin sql_fromtablejoin;




    private sql_Select sql_select;




    private sql_SqlCaseWhen sql_sqlcasewhen;




    private sql_Select sql_select;




    private List<sql_FullExpression> sql_fullexpressions;




    private sql_ExprGroup sql_exprgroup;




    private sql_SQLCaseOperand sql_sqlcaseoperand;


    public sql_OrExpr(
    ) {
        this.sql_fullexpressions = new ArrayList<>();
    }

    public sql_OrExpr(
        ArrayList<sql_FullExpression> sql_fullexpressions    ) {
        this.sql_fullexpressions = sql_fullexpressions;
    }


    public sql_FromTableJoin getSql_fromtablejoin() {
        return sql_fromtablejoin;
    }

    public void setSql_fromtablejoin(sql_FromTableJoin sql_fromtablejoin) {
        this.sql_fromtablejoin = sql_fromtablejoin;
    }
    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }
    public sql_SqlCaseWhen getSql_sqlcasewhen() {
        return sql_sqlcasewhen;
    }

    public void setSql_sqlcasewhen(sql_SqlCaseWhen sql_sqlcasewhen) {
        this.sql_sqlcasewhen = sql_sqlcasewhen;
    }
    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }
    public List<sql_FullExpression> getSql_fullexpressions() {
        return sql_fullexpressions;
    }

    public void addSql_fullexpression(Sql_fullexpression sql_fullexpression) {
        this.sql_fullexpressions.add(sql_fullexpression);
    }
    public sql_ExprGroup getSql_exprgroup() {
        return sql_exprgroup;
    }

    public void setSql_exprgroup(sql_ExprGroup sql_exprgroup) {
        this.sql_exprgroup = sql_exprgroup;
    }
    public sql_SQLCaseOperand getSql_sqlcaseoperand() {
        return sql_sqlcaseoperand;
    }

    public void setSql_sqlcaseoperand(sql_SQLCaseOperand sql_sqlcaseoperand) {
        this.sql_sqlcaseoperand = sql_sqlcaseoperand;
    }

}