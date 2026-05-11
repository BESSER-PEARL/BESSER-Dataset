





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Fk  {

    private String nameFk;
    private String status;
    private String columnReference;
    private String columnName;
    private String type;



    public DML_DDL_Fk(
        String nameFk,        String status,        String columnReference,        String columnName,        String type    ) {
        this.nameFk = nameFk;
        this.status = status;
        this.columnReference = columnReference;
        this.columnName = columnName;
        this.type = type;
    }


    public String getNamefk() {
        return nameFk;
    }

    public void setNamefk(String nameFk) {
        this.nameFk = nameFk;
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
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}