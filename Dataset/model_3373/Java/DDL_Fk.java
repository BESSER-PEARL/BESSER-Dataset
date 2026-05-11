





import java.util.List;
import java.util.ArrayList;

public class DDL_Fk  {

    private String nameFk;
    private String columnName;
    private String status;
    private String columnReference;



    public DDL_Fk(
        String nameFk,        String columnName,        String status,        String columnReference    ) {
        this.nameFk = nameFk;
        this.columnName = columnName;
        this.status = status;
        this.columnReference = columnReference;
    }


    public String getNamefk() {
        return nameFk;
    }

    public void setNamefk(String nameFk) {
        this.nameFk = nameFk;
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
    public String getColumnreference() {
        return columnReference;
    }

    public void setColumnreference(String columnReference) {
        this.columnReference = columnReference;
    }


}