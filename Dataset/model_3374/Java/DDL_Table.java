





import java.util.List;
import java.util.ArrayList;

public class DDL_Table extends DataDefinition {

    private String tableName;
    private String commentTable;





    private List<DDL_Column> ddl_columns;


    public DDL_Table(
        String tableName,        String commentTable    ) {
        super(
        );
        this.tableName = tableName;
        this.commentTable = commentTable;
        this.ddl_columns = new ArrayList<>();
    }

    public DDL_Table(
        String tableName,        String commentTable        ArrayList<DDL_Column> ddl_columns    ) {
        this.tableName = tableName;
        this.commentTable = commentTable;
        this.ddl_columns = ddl_columns;
    }

    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getCommenttable() {
        return commentTable;
    }

    public void setCommenttable(String commentTable) {
        this.commentTable = commentTable;
    }

    public List<DDL_Column> getDdl_columns() {
        return ddl_columns;
    }

    public void addDdl_column(Ddl_column ddl_column) {
        this.ddl_columns.add(ddl_column);
    }

}