





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_Parameter  {

    private String name;





    private SQL2003_V3_DataType sql2003_v3_datatype;


    public SQL2003_V3_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V3_DataType getSql2003_v3_datatype() {
        return sql2003_v3_datatype;
    }

    public void setSql2003_v3_datatype(SQL2003_V3_DataType sql2003_v3_datatype) {
        this.sql2003_v3_datatype = sql2003_v3_datatype;
    }

}