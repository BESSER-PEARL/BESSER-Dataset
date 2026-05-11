





import java.util.List;
import java.util.ArrayList;

public class RDBMS_Table  {

    private boolean is_local;
    private String name;





    private RDBMS_Schema rdbms_schema;


    public RDBMS_Table(
        boolean is_local,        String name    ) {
        this.is_local = is_local;
        this.name = name;
    }


    public boolean getIs_local() {
        return is_local;
    }

    public void setIs_local(boolean is_local) {
        this.is_local = is_local;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RDBMS_Schema getRdbms_schema() {
        return rdbms_schema;
    }

    public void setRdbms_schema(RDBMS_Schema rdbms_schema) {
        this.rdbms_schema = rdbms_schema;
    }

}