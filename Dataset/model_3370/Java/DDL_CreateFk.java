





import java.util.List;
import java.util.ArrayList;

public class DDL_CreateFk  {

    private String columnName;
    private String columnReference;
    private String nameFk;



    public DDL_CreateFk(
        String columnName,        String columnReference,        String nameFk    ) {
        this.columnName = columnName;
        this.columnReference = columnReference;
        this.nameFk = nameFk;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getColumnreference() {
        return columnReference;
    }

    public void setColumnreference(String columnReference) {
        this.columnReference = columnReference;
    }
    public String getNamefk() {
        return nameFk;
    }

    public void setNamefk(String nameFk) {
        this.nameFk = nameFk;
    }


}