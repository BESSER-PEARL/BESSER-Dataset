





import java.util.List;
import java.util.ArrayList;

public class sql_FullExpression extends OrExpr {

    private String isnull;
    private String c;
    private String notPrm;





    private sql_InOper sql_inoper;




    private sql_XExpr sql_xexpr;




    private sql_Like sql_like;




    private sql_Comparison sql_comparison;




    private sql_ExistsOper sql_existsoper;




    private sql_FullExpression sql_fullexpression;




    private sql_Between sql_between;




    private sql_FullExpression sql_fullexpression;




    private sql_ExprGroup sql_exprgroup;


    public sql_FullExpression(
        String isnull,        String c,        String notPrm    ) {
        super(
        );
        this.isnull = isnull;
        this.c = c;
        this.notPrm = notPrm;
    }


    public String getIsnull() {
        return isnull;
    }

    public void setIsnull(String isnull) {
        this.isnull = isnull;
    }
    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }
    public String getNotprm() {
        return notPrm;
    }

    public void setNotprm(String notPrm) {
        this.notPrm = notPrm;
    }

    public sql_InOper getSql_inoper() {
        return sql_inoper;
    }

    public void setSql_inoper(sql_InOper sql_inoper) {
        this.sql_inoper = sql_inoper;
    }
    public sql_XExpr getSql_xexpr() {
        return sql_xexpr;
    }

    public void setSql_xexpr(sql_XExpr sql_xexpr) {
        this.sql_xexpr = sql_xexpr;
    }
    public sql_Like getSql_like() {
        return sql_like;
    }

    public void setSql_like(sql_Like sql_like) {
        this.sql_like = sql_like;
    }
    public sql_Comparison getSql_comparison() {
        return sql_comparison;
    }

    public void setSql_comparison(sql_Comparison sql_comparison) {
        this.sql_comparison = sql_comparison;
    }
    public sql_ExistsOper getSql_existsoper() {
        return sql_existsoper;
    }

    public void setSql_existsoper(sql_ExistsOper sql_existsoper) {
        this.sql_existsoper = sql_existsoper;
    }
    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }
    public sql_Between getSql_between() {
        return sql_between;
    }

    public void setSql_between(sql_Between sql_between) {
        this.sql_between = sql_between;
    }
    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }
    public sql_ExprGroup getSql_exprgroup() {
        return sql_exprgroup;
    }

    public void setSql_exprgroup(sql_ExprGroup sql_exprgroup) {
        this.sql_exprgroup = sql_exprgroup;
    }

}