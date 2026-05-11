





import java.util.List;
import java.util.ArrayList;

public class DDL_Ck  {

    private String nameCk;
    private String status;





    private DDL_Table ddl_table;


    public DDL_Ck(
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

    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }

}