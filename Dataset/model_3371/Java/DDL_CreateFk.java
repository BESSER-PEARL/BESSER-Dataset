





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateFk  {

    private String columnName;
    private String nameFk;
    private String columnReference;



    public DDL_CreateFk(
        String columnName,        String nameFk,        String columnReference    ) {
        this.columnName = columnName;
        this.nameFk = nameFk;
        this.columnReference = columnReference;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getNamefk() {
        return nameFk;
    }

    public void setNamefk(String nameFk) {
        this.nameFk = nameFk;
    }
    public String getColumnreference() {
        return columnReference;
    }

    public void setColumnreference(String columnReference) {
        this.columnReference = columnReference;
    }


}