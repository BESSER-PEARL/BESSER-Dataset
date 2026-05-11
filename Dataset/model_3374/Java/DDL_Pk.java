





import java.util.List;
import java.util.ArrayList;

public class DDL_Pk  {

    private String columnName;
    private String namePk;





    private DDL_Table ddl_table;


    public DDL_Pk(
        String columnName,        String namePk    ) {
        this.columnName = columnName;
        this.namePk = namePk;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getNamepk() {
        return namePk;
    }

    public void setNamepk(String namePk) {
        this.namePk = namePk;
    }

    public DDL_Table getDdl_table() {
        return ddl_table;
    }

    public void setDdl_table(DDL_Table ddl_table) {
        this.ddl_table = ddl_table;
    }

}