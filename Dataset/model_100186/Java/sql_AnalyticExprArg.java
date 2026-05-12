





import java.util.List;
import java.util.ArrayList;

public class sql_AnalyticExprArg extends AnalyticExprArgs {






    private sql_WindowingClauseOperandPreceding sql_windowingclauseoperandpreceding;




    private sql_DbObjectName sql_dbobjectname;




    private sql_Operands sql_operands;


    public sql_AnalyticExprArg(
    ) {
        super(
        );
    }



    public sql_WindowingClauseOperandPreceding getSql_windowingclauseoperandpreceding() {
        return sql_windowingclauseoperandpreceding;
    }

    public void setSql_windowingclauseoperandpreceding(sql_WindowingClauseOperandPreceding sql_windowingclauseoperandpreceding) {
        this.sql_windowingclauseoperandpreceding = sql_windowingclauseoperandpreceding;
    }
    public sql_DbObjectName getSql_dbobjectname() {
        return sql_dbobjectname;
    }

    public void setSql_dbobjectname(sql_DbObjectName sql_dbobjectname) {
        this.sql_dbobjectname = sql_dbobjectname;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }

}