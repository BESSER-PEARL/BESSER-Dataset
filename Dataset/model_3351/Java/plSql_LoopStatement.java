





import java.util.List;
import java.util.ArrayList;

public class plSql_LoopStatement extends Statement {

    private String endLabel;





    private List<plSql_Statement> plsql_statements;


    public plSql_LoopStatement(
        String endLabel    ) {
        super(
        );
        this.endLabel = endLabel;
        this.plsql_statements = new ArrayList<>();
    }

    public plSql_LoopStatement(
        String endLabel        ArrayList<plSql_Statement> plsql_statements    ) {
        this.endLabel = endLabel;
        this.plsql_statements = plsql_statements;
    }

    public String getEndlabel() {
        return endLabel;
    }

    public void setEndlabel(String endLabel) {
        this.endLabel = endLabel;
    }

    public List<plSql_Statement> getPlsql_statements() {
        return plsql_statements;
    }

    public void addPlsql_statement(Plsql_statement plsql_statement) {
        this.plsql_statements.add(plsql_statement);
    }

}