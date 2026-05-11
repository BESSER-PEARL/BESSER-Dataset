





import java.util.List;
import java.util.ArrayList;

public class sql_InOper  {

    private String op;





    private sql_SubQueryOperand sql_subqueryoperand;


    public sql_InOper(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public sql_SubQueryOperand getSql_subqueryoperand() {
        return sql_subqueryoperand;
    }

    public void setSql_subqueryoperand(sql_SubQueryOperand sql_subqueryoperand) {
        this.sql_subqueryoperand = sql_subqueryoperand;
    }

}