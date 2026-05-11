





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Fk  {

    private String columnName;
    private String status;
    private String nameFk;
    private String columnReference;



    public DML_DDL_Fk(
        String columnName,        String status,        String nameFk,        String columnReference    ) {
        this.columnName = columnName;
        this.status = status;
        this.nameFk = nameFk;
        this.columnReference = columnReference;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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