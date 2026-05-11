





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_CommentTable extends DataDefinition {

    private String tableName;
    private String tableComment;



    public DML_DDL_CommentTable(
        String tableName,        String tableComment    ) {
        super(
        );
        this.tableName = tableName;
        this.tableComment = tableComment;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getTablecomment() {
        return tableComment;
    }

    public void setTablecomment(String tableComment) {
        this.tableComment = tableComment;
    }


}