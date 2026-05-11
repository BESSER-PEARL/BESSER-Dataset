





import java.util.List;
import java.util.ArrayList;

public class DDL_Type  {

    private String name;





    private DDL_DataType ddl_datatype;


    public DDL_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DDL_DataType getDdl_datatype() {
        return ddl_datatype;
    }

    public void setDdl_datatype(DDL_DataType ddl_datatype) {
        this.ddl_datatype = ddl_datatype;
    }

}