





import java.util.List;
import java.util.ArrayList;

public class rdbms_tables  {

    private String group;





    private rdbms_schema rdbms_schema;




    private List<rdbms_table> rdbms_tables;




    private rdbms_DocumentRoot rdbms_documentroot;


    public rdbms_tables(
        String group    ) {
        this.group = group;
        this.rdbms_tables = new ArrayList<>();
    }

    public rdbms_tables(
        String group        ArrayList<rdbms_table> rdbms_tables    ) {
        this.group = group;
        this.rdbms_tables = rdbms_tables;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public rdbms_schema getRdbms_schema() {
        return rdbms_schema;
    }

    public void setRdbms_schema(rdbms_schema rdbms_schema) {
        this.rdbms_schema = rdbms_schema;
    }
    public List<rdbms_table> getRdbms_tables() {
        return rdbms_tables;
    }

    public void addRdbms_table(Rdbms_table rdbms_table) {
        this.rdbms_tables.add(rdbms_table);
    }
    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }

}