





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Pk  {

    private String columnName;
    private String namePk;





    private DML_DDL_Table dml_ddl_table;


    public DML_DDL_Pk(
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

    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }

}