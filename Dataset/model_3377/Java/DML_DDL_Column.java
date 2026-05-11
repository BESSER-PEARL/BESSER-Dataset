





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Column  {

    private int scale;
    private String commentColumn;
    private boolean columnNull;
    private int precision;
    private String columnName;





    private DML_DDL_Type dml_ddl_type;




    private DML_DDL_Table dml_ddl_table;


    public DML_DDL_Column(
        int scale,        String commentColumn,        boolean columnNull,        int precision,        String columnName    ) {
        this.scale = scale;
        this.commentColumn = commentColumn;
        this.columnNull = columnNull;
        this.precision = precision;
        this.columnName = columnName;
    }


    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }
    public String getCommentcolumn() {
        return commentColumn;
    }

    public void setCommentcolumn(String commentColumn) {
        this.commentColumn = commentColumn;
    }
    public boolean getColumnnull() {
        return columnNull;
    }

    public void setColumnnull(boolean columnNull) {
        this.columnNull = columnNull;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public DML_DDL_Type getDml_ddl_type() {
        return dml_ddl_type;
    }

    public void setDml_ddl_type(DML_DDL_Type dml_ddl_type) {
        this.dml_ddl_type = dml_ddl_type;
    }
    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }

}