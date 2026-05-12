





import java.util.List;
import java.util.ArrayList;

public class sql_Between  {

    private String opBetween;





    private sql_Operands sql_operands;




    private sql_FullExpression sql_fullexpression;




    private sql_Operands sql_operands;


    public sql_Between(
        String opBetween    ) {
        this.opBetween = opBetween;
    }


    public String getOpbetween() {
        return opBetween;
    }

    public void setOpbetween(String opBetween) {
        this.opBetween = opBetween;
    }

    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
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