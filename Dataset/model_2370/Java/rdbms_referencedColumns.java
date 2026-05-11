





import java.util.List;
import java.util.ArrayList;

public class rdbms_referencedColumns  {

    private String group;





    private rdbms_DocumentRoot rdbms_documentroot;




    private rdbms_key rdbms_key;




    private rdbms_foreignKey rdbms_foreignkey;




    private List<rdbms_oID> rdbms_oids;


    public rdbms_referencedColumns(
        String group    ) {
        this.group = group;
        this.rdbms_oids = new ArrayList<>();
    }

    public rdbms_referencedColumns(
        String group        ArrayList<rdbms_oID> rdbms_oids    ) {
        this.group = group;
        this.rdbms_oids = rdbms_oids;
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
    public rdbms_key getRdbms_key() {
        return rdbms_key;
    }

    public void setRdbms_key(rdbms_key rdbms_key) {
        this.rdbms_key = rdbms_key;
    }
    public rdbms_foreignKey getRdbms_foreignkey() {
        return rdbms_foreignkey;
    }

    public void setRdbms_foreignkey(rdbms_foreignKey rdbms_foreignkey) {
        this.rdbms_foreignkey = rdbms_foreignkey;
    }
    public List<rdbms_oID> getRdbms_oids() {
        return rdbms_oids;
    }

    public void addRdbms_oid(Rdbms_oid rdbms_oid) {
        this.rdbms_oids.add(rdbms_oid);
    }

}