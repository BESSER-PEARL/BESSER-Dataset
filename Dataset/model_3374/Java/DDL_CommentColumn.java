





import java.util.List;
import java.util.ArrayList;

public class DDL_CommentColumn extends DataDefinition {

    private String columnComment;
    private String tableName;
    private String columnName;



    public DDL_CommentColumn(
        String columnComment,        String tableName,        String columnName    ) {
        super(
        );
        this.columnComment = columnComment;
        this.tableName = tableName;
        this.columnName = columnName;
    }


    public String getColumncomment() {
        return columnComment;
    }

    public void setColumncomment(String columnComment) {
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


}