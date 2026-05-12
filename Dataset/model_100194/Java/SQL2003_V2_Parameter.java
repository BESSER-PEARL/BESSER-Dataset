





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_Parameter  {

    private String name;





    private SQL2003_V2_DataType sql2003_v2_datatype;


    public SQL2003_V2_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V2_DataType getSql2003_v2_datatype() {
        return sql2003_v2_datatype;
    }

    public void setSql2003_v2_datatype(SQL2003_V2_DataType sql2003_v2_datatype) {
        this.sql2003_v2_datatype = sql2003_v2_datatype;
    }

}