





import java.util.List;
import java.util.ArrayList;

public class rdb_Style  {

    private String columnName;
    private String columnPrimaryKey;
    private String tableTitle;
    private String columnComment;
    private String columnNullCheck;
    private String grid;
    private String columnType;



    public rdb_Style(
        String columnName,        String columnPrimaryKey,        String tableTitle,        String columnComment,        String columnNullCheck,        String grid,        String columnType    ) {
        this.columnName = columnName;
        this.columnPrimaryKey = columnPrimaryKey;
        this.tableTitle = tableTitle;
        this.columnComment = columnComment;
        this.columnNullCheck = columnNullCheck;
        this.grid = grid;
        this.columnType = columnType;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getColumnprimarykey() {
        return columnPrimaryKey;
    }

    public void setColumnprimarykey(String columnPrimaryKey) {
        this.columnPrimaryKey = columnPrimaryKey;
    }
    public String getTabletitle() {
        return tableTitle;
    }

    public void setTabletitle(String tableTitle) {
        this.tableTitle = tableTitle;
    }
    public String getColumncomment() {
        return columnComment;
    }

    public void setColumncomment(String columnComment) {
        this.columnComment = columnComment;
    }
    public String getColumnnullcheck() {
        return columnNullCheck;
    }

    public void setColumnnullcheck(String columnNullCheck) {
        this.columnNullCheck = columnNullCheck;
    }
    public String getGrid() {
        return grid;
    }

    public void setGrid(String grid) {
        this.grid = grid;
    }
    public String getColumntype() {
        return columnType;
    }

    public void setColumntype(String columnType) {
        this.columnType = columnType;
    }


}