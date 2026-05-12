





import java.util.List;
import java.util.ArrayList;

public class SQL2003_Parameter  {

    private String name;





    private SQL2003_DataType sql2003_datatype;


    public SQL2003_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_DataType getSql2003_datatype() {
        return sql2003_datatype;
    }

    public void setSql2003_datatype(SQL2003_DataType sql2003_datatype) {
        this.sql2003_datatype = sql2003_datatype;
    }

}