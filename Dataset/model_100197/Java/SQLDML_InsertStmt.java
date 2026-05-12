





import java.util.List;
import java.util.ArrayList;

public class SQLDML_InsertStmt extends Statement {

    private String tableName;



    public SQLDML_InsertStmt(
        String tableName    ) {
        super(
        );
        this.tableName = tableName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }


}