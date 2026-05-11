





import java.util.List;
import java.util.ArrayList;

public class DDL_Column  {

    private boolean columnNull;
    private String commentColumn;
    private String columnName;





    private DDL_Type ddl_type;


    public DDL_Column(
        boolean columnNull,        String commentColumn,        String columnName    ) {
        this.columnNull = columnNull;
        this.commentColumn = commentColumn;
        this.columnName = columnName;
    }


    public boolean getColumnnull() {
        return columnNull;
    }

    public void setColumnnull(boolean columnNull) {
        this.columnNull = columnNull;
    }
    public String getCommentcolumn() {
        return commentColumn;
    }

    public void setCommentcolumn(String commentColumn) {
        this.commentColumn = commentColumn;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public DDL_Type getDdl_type() {
        return ddl_type;
    }

    public void setDdl_type(DDL_Type ddl_type) {
        this.ddl_type = ddl_type;
    }

}