





import java.util.List;
import java.util.ArrayList;

public class DML_Value  {

    private String value;





    private DML_Registry dml_registry;




    private DML_Column dml_column;


    public DML_Value(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public DML_Registry getDml_registry() {
        return dml_registry;
    }

    public void setDml_registry(DML_Registry dml_registry) {
        this.dml_registry = dml_registry;
    }
    public DML_Column getDml_column() {
        return dml_column;
    }

    public void setDml_column(DML_Column dml_column) {
        this.dml_column = dml_column;
    }

}