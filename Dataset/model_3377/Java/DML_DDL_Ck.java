





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Ck  {

    private String nameCk;
    private String status;





    private DML_DDL_Table dml_ddl_table;


    public DML_DDL_Ck(
        String nameCk,        String status    ) {
        this.nameCk = nameCk;
        this.status = status;
    }


    public String getNameck() {
        return nameCk;
    }

    public void setNameck(String nameCk) {
        this.nameCk = nameCk;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }

}