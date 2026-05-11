





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Column  {

    private boolean columnNull;
    private String columnName;
    private String commentColumn;





    private DML_DDL_Table dml_ddl_table;




    private DML_DDL_Type dml_ddl_type;


    public DML_DDL_Column(
        boolean columnNull,        String columnName,        String commentColumn    ) {
        this.columnNull = columnNull;
        this.columnName = columnName;
        this.commentColumn = commentColumn;
    }


    public boolean getColumnnull() {
        return columnNull;
    }

    public void setColumnnull(boolean columnNull) {
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

    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }
    public DML_DDL_Type getDml_ddl_type() {
        return dml_ddl_type;
    }

    public void setDml_ddl_type(DML_DDL_Type dml_ddl_type) {
        this.dml_ddl_type = dml_ddl_type;
    }

}