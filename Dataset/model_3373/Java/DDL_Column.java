





import java.util.List;
import java.util.ArrayList;

public class DDL_Column  {

    private String columnName;
    private int precision;
    private int scale;
    private boolean columnNull;
    private String commentColumn;





    private DDL_Type ddl_type;




    private DDL_Table ddl_table;


    public DDL_Column(
        String columnName,        int precision,        int scale,        boolean columnNull,        String commentColumn    ) {
        this.columnName = columnName;
        this.precision = precision;
        this.scale = scale;
        this.columnNull = columnNull;
        this.commentColumn = commentColumn;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
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

    public DDL_Type getDdl_type() {
        return ddl_type;
    }

    public void setDdl_type(DDL_Type ddl_type) {
        this.ddl_type = ddl_type;
    }
    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }

}