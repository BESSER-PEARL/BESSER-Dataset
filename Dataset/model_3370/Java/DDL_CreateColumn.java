





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateColumn  {

    private String columnName;
    private String commentColumn;
    private String columnType;
    private boolean columnNull;





    private DDL_CreateTable ddl_createtable;


    public DDL_CreateColumn(
        String columnName,        String commentColumn,        String columnType,        boolean columnNull    ) {
        this.columnName = columnName;
        this.commentColumn = commentColumn;
        this.columnType = columnType;
        this.columnNull = columnNull;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getCommentcolumn() {
        return commentColumn;
    }

    public void setCommentcolumn(String commentColumn) {
        this.commentColumn = commentColumn;
    }
    public String getColumntype() {
        return columnType;
    }

    public void setColumntype(String columnType) {
        this.columnType = columnType;
    }
    public boolean getColumnnull() {
        return columnNull;
    }

    public void setColumnnull(boolean columnNull) {
        this.columnNull = columnNull;
    }

    public DDL_CreateTable getDdl_createtable() {
        return ddl_createtable;
    }

    public void setDdl_createtable(DDL_CreateTable ddl_createtable) {
        this.ddl_createtable = ddl_createtable;
    }

}