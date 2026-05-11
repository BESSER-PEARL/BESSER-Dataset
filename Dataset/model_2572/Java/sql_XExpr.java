





import java.util.List;
import java.util.ArrayList;

public class sql_XExpr  {

    private String xf;





    private sql_FullExpression sql_fullexpression;




    private sql_Operands sql_operands;


    public sql_XExpr(
        String xf    ) {
        this.xf = xf;
    }


    public String getXf() {
        return xf;
    }

    public void setXf(String xf) {
        this.xf = xf;
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