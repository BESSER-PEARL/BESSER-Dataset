





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Value  {

    private String value;





    private DML_DDL_Column dml_ddl_column;




    private DML_DDL_Registry dml_ddl_registry;


    public DML_DDL_Value(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public DML_DDL_Column getDml_ddl_column() {
        return dml_ddl_column;
    }

    public void setDml_ddl_column(DML_DDL_Column dml_ddl_column) {
        this.dml_ddl_column = dml_ddl_column;
    }
    public DML_DDL_Registry getDml_ddl_registry() {
        return dml_ddl_registry;
    }

    public void setDml_ddl_registry(DML_DDL_Registry dml_ddl_registry) {
        this.dml_ddl_registry = dml_ddl_registry;
    }

}