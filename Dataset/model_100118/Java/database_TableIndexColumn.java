





import java.util.List;
import java.util.ArrayList;

public class database_TableIndexColumn extends ExtensibleModel {

    private String columnType;
    private String columnName;
    private boolean ascending;



    public database_TableIndexColumn(
        String columnType,        String columnName,        boolean ascending    ) {
        super(
        );
        this.columnType = columnType;
        this.columnName = columnName;
        this.ascending = ascending;
    }


    public String getColumntype() {
        return columnType;
    }

    public void setColumntype(String columnType) {
        this.columnType = columnType;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public boolean getAscending() {
        return ascending;
    }

    public void setAscending(boolean ascending) {
        this.ascending = ascending;
    }


}