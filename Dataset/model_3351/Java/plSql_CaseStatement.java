





import java.util.List;
import java.util.ArrayList;

public class plSql_CaseStatement extends Statement {

    private String endLabel;





    private plSql_Expression plsql_expression;


    public plSql_CaseStatement(
        String endLabel    ) {
        super(
        );
        this.endLabel = endLabel;
    }


    public String getEndlabel() {
        return endLabel;
    }

    public void setEndlabel(String endLabel) {
        this.endLabel = endLabel;
    }

    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }

}