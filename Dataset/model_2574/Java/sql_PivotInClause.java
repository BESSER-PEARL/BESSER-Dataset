





import java.util.List;
import java.util.ArrayList;

public class sql_PivotInClause  {

    private String pinany;





    private sql_PivotTable sql_pivottable;




    private sql_SubQueryOperand sql_subqueryoperand;


    public sql_PivotInClause(
        String pinany    ) {
        this.pinany = pinany;
    }


    public String getPinany() {
        return pinany;
    }

    public void setPinany(String pinany) {
        this.pinany = pinany;
    }

    public sql_PivotTable getSql_pivottable() {
        return sql_pivottable;
    }

    public void setSql_pivottable(sql_PivotTable sql_pivottable) {
        this.sql_pivottable = sql_pivottable;
    }
    public sql_SubQueryOperand getSql_subqueryoperand() {
        return sql_subqueryoperand;
    }

    public void setSql_subqueryoperand(sql_SubQueryOperand sql_subqueryoperand) {
        this.sql_subqueryoperand = sql_subqueryoperand;
    }

}