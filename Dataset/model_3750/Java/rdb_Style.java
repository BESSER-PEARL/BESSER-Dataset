





import java.util.List;
import java.util.ArrayList;

public class rdb_Style  {

    private String columnPrimaryKey;
    private String tableTitle;
    private String columnNullCheck;
    private String columnName;
    private String scale;
    private String columnType;
    private String grid;
    private String columnComment;



    public rdb_Style(
        String columnPrimaryKey,        String tableTitle,        String columnNullCheck,        String columnName,        String scale,        String columnType,        String grid,        String columnComment    ) {
        this.columnPrimaryKey = columnPrimaryKey;
        this.tableTitle = tableTitle;
        this.columnNullCheck = columnNullCheck;
        this.columnName = columnName;
        this.scale = scale;
        this.columnType = columnType;
        this.grid = grid;
        this.columnComment = columnComment;
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
    public String getColumnnullcheck() {
        return columnNullCheck;
    }

    public void setColumnnullcheck(String columnNullCheck) {
        this.columnNullCheck = columnNullCheck;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getColumntype() {
        return columnType;
    }

    public void setColumntype(String columnType) {
        this.columnType = columnType;
    }
    public String getGrid() {
        return grid;
    }

    public void setGrid(String grid) {
        this.grid = grid;
    }
    public String getColumncomment() {
        return columnComment;
    }

    public void setColumncomment(String columnComment) {
        this.columnComment = columnComment;
    }


}