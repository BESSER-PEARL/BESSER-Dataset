





import java.util.List;
import java.util.ArrayList;

public class DDL_CommentColumn extends DataDefinition {

    private String tableName;
    private String columnComment;
    private String columnName;



    public DDL_CommentColumn(
        String tableName,        String columnComment,        String columnName    ) {
        super(
        );
        this.tableName = tableName;
        this.columnComment = columnComment;
        this.columnName = columnName;
    }


    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
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


}