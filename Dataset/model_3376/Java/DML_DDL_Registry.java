





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Registry  {






    private List<DML_DDL_Value> dml_ddl_values;




    private DML_DDL_Table dml_ddl_table;


    public DML_DDL_Registry(
    ) {
        this.dml_ddl_values = new ArrayList<>();
    }

    public DML_DDL_Registry(
        ArrayList<DML_DDL_Value> dml_ddl_values    ) {
        this.dml_ddl_values = dml_ddl_values;
    }


    public List<DML_DDL_Value> getDml_ddl_values() {
        return dml_ddl_values;
    }

    public void addDml_ddl_value(Dml_ddl_value dml_ddl_value) {
        this.dml_ddl_values.add(dml_ddl_value);
    }
    public DML_DDL_Table getDml_ddl_table() {
        return dml_ddl_table;
    }

    public void setDml_ddl_table(DML_DDL_Table dml_ddl_table) {
        this.dml_ddl_table = dml_ddl_table;
    }

}