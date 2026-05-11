





import java.util.List;
import java.util.ArrayList;

public class plSql_ContinueStatement extends Statement {

    private String labelName;





    private plSql_Expression plsql_expression;


    public plSql_ContinueStatement(
        String labelName    ) {
        super(
        );
        this.labelName = labelName;
    }


    public String getLabelname() {
        return labelName;
    }

    public void setLabelname(String labelName) {
        this.labelName = labelName;
    }

    public plSql_Expression getPlsql_expression() {
        return plsql_expression;
    }

    public void setPlsql_expression(plSql_Expression plsql_expression) {
        this.plsql_expression = plsql_expression;
    }

}