





import java.util.List;
import java.util.ArrayList;

public class rdpl_Table  {

    private String name;





    private rdpl_Schema rdpl_schema;




    private rdpl_ForeignKey rdpl_foreignkey;




    private List<rdpl_ForeignKey> rdpl_foreignkeys;


    public rdpl_Table(
        String name    ) {
        this.name = name;
        this.rdpl_foreignkeys = new ArrayList<>();
    }

    public rdpl_Table(
        String name        ArrayList<rdpl_ForeignKey> rdpl_foreignkeys    ) {
        this.name = name;
        this.rdpl_foreignkeys = rdpl_foreignkeys;
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
    public rdpl_ForeignKey getRdpl_foreignkey() {
        return rdpl_foreignkey;
    }

    public void setRdpl_foreignkey(rdpl_ForeignKey rdpl_foreignkey) {
        this.rdpl_foreignkey = rdpl_foreignkey;
    }
    public List<rdpl_ForeignKey> getRdpl_foreignkeys() {
        return rdpl_foreignkeys;
    }

    public void addRdpl_foreignkey(Rdpl_foreignkey rdpl_foreignkey) {
        this.rdpl_foreignkeys.add(rdpl_foreignkey);
    }

}