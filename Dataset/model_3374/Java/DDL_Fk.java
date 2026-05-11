





import java.util.List;
import java.util.ArrayList;

public class DDL_Fk  {

    private String columnName;
    private String status;
    private String columnReference;
    private String nameFk;





    private DDL_Table ddl_table;




    private DDL_Table ddl_table;


    public DDL_Fk(
        String columnName,        String status,        String columnReference,        String nameFk    ) {
        this.columnName = columnName;
        this.status = status;
        this.columnReference = columnReference;
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
    public String getNamefk() {
        return nameFk;
    }

    public void setNamefk(String nameFk) {
        this.nameFk = nameFk;
    }

    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }
    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }

}