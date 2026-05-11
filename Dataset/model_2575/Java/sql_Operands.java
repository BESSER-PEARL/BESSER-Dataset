





import java.util.List;
import java.util.ArrayList;

public class sql_Operands extends OpFunctionArgAgregate {






    private sql_XExpr sql_xexpr;




    private sql_FullExpression sql_fullexpression;




    private sql_Between sql_between;




    private sql_OpFunctionCast sql_opfunctioncast;




    private sql_Comparison sql_comparison;




    private sql_Operands sql_operands;




    private sql_FunctionExtract sql_functionextract;




    private sql_Between sql_between;




    private sql_SQLCaseOperand sql_sqlcaseoperand;


    public sql_Operands(
    ) {
        super(
        );
    }



    public sql_XExpr getSql_xexpr() {
        return sql_xexpr;
    }

    public void setSql_xexpr(sql_XExpr sql_xexpr) {
        this.sql_xexpr = sql_xexpr;
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
    public sql_OpFunctionCast getSql_opfunctioncast() {
        return sql_opfunctioncast;
    }

    public void setSql_opfunctioncast(sql_OpFunctionCast sql_opfunctioncast) {
        this.sql_opfunctioncast = sql_opfunctioncast;
    }
    public sql_Comparison getSql_comparison() {
        return sql_comparison;
    }

    public void setSql_comparison(sql_Comparison sql_comparison) {
        this.sql_comparison = sql_comparison;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }
    public sql_FunctionExtract getSql_functionextract() {
        return sql_functionextract;
    }

    public void setSql_functionextract(sql_FunctionExtract sql_functionextract) {
        this.sql_functionextract = sql_functionextract;
    }
    public sql_Between getSql_between() {
        return sql_between;
    }

    public void setSql_between(sql_Between sql_between) {
        this.sql_between = sql_between;
    }
    public sql_SQLCaseOperand getSql_sqlcaseoperand() {
        return sql_sqlcaseoperand;
    }

    public void setSql_sqlcaseoperand(sql_SQLCaseOperand sql_sqlcaseoperand) {
        this.sql_sqlcaseoperand = sql_sqlcaseoperand;
    }

}