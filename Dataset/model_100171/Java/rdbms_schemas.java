





import java.util.List;
import java.util.ArrayList;

public class rdbms_schemas  {

    private String group;





    private List<rdbms_schema> rdbms_schemas;




    private rdbms_DocumentRoot rdbms_documentroot;


    public rdbms_schemas(
        String group    ) {
        this.group = group;
        this.rdbms_schemas = new ArrayList<>();
    }

    public rdbms_schemas(
        String group        ArrayList<rdbms_schema> rdbms_schemas    ) {
        this.group = group;
        this.rdbms_schemas = rdbms_schemas;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<rdbms_schema> getRdbms_schemas() {
        return rdbms_schemas;
    }

    public void addRdbms_schema(Rdbms_schema rdbms_schema) {
        this.rdbms_schemas.add(rdbms_schema);
    }
    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }

}