





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_Parameter  {

    private String name;





    private SQL2003_evo_DataType sql2003_evo_datatype;


    public SQL2003_evo_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_evo_DataType getSql2003_evo_datatype() {
        return sql2003_evo_datatype;
    }

    public void setSql2003_evo_datatype(SQL2003_evo_DataType sql2003_evo_datatype) {
        this.sql2003_evo_datatype = sql2003_evo_datatype;
    }

}