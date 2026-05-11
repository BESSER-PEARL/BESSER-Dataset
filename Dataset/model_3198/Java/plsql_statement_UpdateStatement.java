





import java.util.List;
import java.util.ArrayList;

public class plsql_statement_UpdateStatement extends ModifySQLStatement {

    private String table;



    public plsql_statement_UpdateStatement(
        String table    ) {
        super(
        );
        this.table = table;
    }


    public String getTable() {
        return table;
    }

    public void setTable(String table) {
        this.table = table;
    }


}