





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Column  {

    private boolean columnNull;
    private String commentColumn;
    private String columnName;





    private DML_DDL_Table dml_ddl_table;


    public DML_DDL_Column(
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

    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }

}