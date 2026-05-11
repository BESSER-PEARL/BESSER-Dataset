





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_CommentColumn extends DataDefinition {

    private String tableName;
    private String columnName;
    private String columnComment;



    public DML_DDL_CommentColumn(
        String tableName,        String columnName,        String columnComment    ) {
        super(
        );
        this.tableName = tableName;
        this.columnName = columnName;
        this.columnComment = columnComment;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getColumncomment() {
        return columnComment;
    }

    public void setColumncomment(String columnComment) {
        this.columnComment = columnComment;
    }


}