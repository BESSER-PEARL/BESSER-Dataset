





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Ck  {

    private String status;
    private String nameCk;





    private DML_DDL_Table dml_ddl_table;


    public DML_DDL_Ck(
        String status,        String nameCk    ) {
        this.status = status;
        this.nameCk = nameCk;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getNameck() {
        return nameCk;
    }

    public void setNameck(String nameCk) {
        this.nameCk = nameCk;
    }

    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }

}