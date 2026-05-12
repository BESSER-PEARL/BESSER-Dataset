





import java.util.List;
import java.util.ArrayList;

public class sql_FullExpression extends OrExpr {

    private String notPrm;
    private String c;
    private String isnull;





    private sql_FullExpression sql_fullexpression;




    private sql_OrExpr sql_orexpr;




    private sql_FullExpression sql_fullexpression;




    private sql_Operands sql_operands;


    public sql_FullExpression(
        String notPrm,        String c,        String isnull    ) {
        super(
        );
        this.notPrm = notPrm;
        this.c = c;
        this.isnull = isnull;
    }


    public String getNotprm() {
        return notPrm;
    }

    public void setNotprm(String notPrm) {
        this.notPrm = notPrm;
    }
    public String getC() {
        return c;
    }

    public void setC(String c) {
        this.c = c;
    }
    public String getIsnull() {
        return isnull;
    }

    public void setIsnull(String isnull) {
        this.isnull = isnull;
    }

    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }
    public sql_OrExpr getSql_orexpr() {
        return sql_orexpr;
    }

    public void setSql_orexpr(sql_OrExpr sql_orexpr) {
        this.sql_orexpr = sql_orexpr;
    }
    public sql_FullExpression getSql_fullexpression() {
        return sql_fullexpression;
    }

    public void setSql_fullexpression(sql_FullExpression sql_fullexpression) {
        this.sql_fullexpression = sql_fullexpression;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }

}