





import java.util.List;
import java.util.ArrayList;

public class dDL_TYPE  {

    private String id;





    private dDL_Column ddl_column;


    public dDL_TYPE(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dDL_Column getDdl_column() {
        return ddl_column;
    }

    public void setDdl_column(dDL_Column ddl_column) {
        this.ddl_column = ddl_column;
    }

}