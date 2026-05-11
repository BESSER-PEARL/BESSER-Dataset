





import java.util.List;
import java.util.ArrayList;

public class rdpl_Type  {

    private String name;





    private rdpl_Schema rdpl_schema;


    public rdpl_Type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rdpl_Schema getRdpl_schema() {
        return rdpl_schema;
    }

    public void setRdpl_schema(rdpl_Schema rdpl_schema) {
        this.rdpl_schema = rdpl_schema;
    }

}