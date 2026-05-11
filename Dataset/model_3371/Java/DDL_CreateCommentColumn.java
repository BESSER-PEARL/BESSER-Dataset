





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateCommentColumn extends DataDefinition {

    private String columnName;
    private String columnComment;
    private String tableName;



    public DDL_CreateCommentColumn(
        String columnName,        String columnComment,        String tableName    ) {
        super(
        );
        this.columnName = columnName;
        this.columnComment = columnComment;
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
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }


}