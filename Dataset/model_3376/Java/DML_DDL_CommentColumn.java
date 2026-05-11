





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_CommentColumn extends DataDefinition {

    private String columnComment;
    private String columnName;
    private String tableName;



    public DML_DDL_CommentColumn(
        String columnComment,        String columnName,        String tableName    ) {
        super(
        );
        this.columnComment = columnComment;
        this.columnName = columnName;
        this.tableName = tableName;
    }


    public String getColumncomment() {
        return columnComment;
    }

    public void setColumncomment(String columnComment) {
        this.columnComment = columnComment;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }


}