





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_Type  {

    private String name;





    private DML_DDL_Column dml_ddl_column;




    private DML_DDL_DataType dml_ddl_datatype;


    public DML_DDL_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DML_DDL_Column getDml_ddl_column() {
        return dml_ddl_column;
    }

    public void setDml_ddl_column(DML_DDL_Column dml_ddl_column) {
        this.dml_ddl_column = dml_ddl_column;
    }
    public DML_DDL_DataType getDml_ddl_datatype() {
        return dml_ddl_datatype;
    }

    public void setDml_ddl_datatype(DML_DDL_DataType dml_ddl_datatype) {
        this.dml_ddl_datatype = dml_ddl_datatype;
    }

}