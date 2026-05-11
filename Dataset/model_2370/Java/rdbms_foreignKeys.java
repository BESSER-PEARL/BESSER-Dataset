





import java.util.List;
import java.util.ArrayList;

public class rdbms_foreignKeys  {

    private String group;





    private rdbms_DocumentRoot rdbms_documentroot;




    private List<rdbms_foreignKey> rdbms_foreignkeys;


    public rdbms_foreignKeys(
        String group    ) {
        this.group = group;
        this.rdbms_foreignkeys = new ArrayList<>();
    }

    public rdbms_foreignKeys(
        String group        ArrayList<rdbms_foreignKey> rdbms_foreignkeys    ) {
        this.group = group;
        this.rdbms_foreignkeys = rdbms_foreignkeys;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }
    public List<rdbms_foreignKey> getRdbms_foreignkeys() {
        return rdbms_foreignkeys;
    }

    public void addRdbms_foreignkey(Rdbms_foreignkey rdbms_foreignkey) {
        this.rdbms_foreignkeys.add(rdbms_foreignkey);
    }

}