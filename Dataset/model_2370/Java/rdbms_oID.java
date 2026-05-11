





import java.util.List;
import java.util.ArrayList;

public class rdbms_oID  {

    private String oID;





    private rdbms_DocumentRoot rdbms_documentroot;




    private rdbms_hasForeignKeys rdbms_hasforeignkeys;




    private rdbms_referencedKeys rdbms_referencedkeys;


    public rdbms_oID(
        String oID    ) {
        this.oID = oID;
    }


    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }

    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }
    public rdbms_hasForeignKeys getRdbms_hasforeignkeys() {
        return rdbms_hasforeignkeys;
    }

    public void setRdbms_hasforeignkeys(rdbms_hasForeignKeys rdbms_hasforeignkeys) {
        this.rdbms_hasforeignkeys = rdbms_hasforeignkeys;
    }
    public rdbms_referencedKeys getRdbms_referencedkeys() {
        return rdbms_referencedkeys;
    }

    public void setRdbms_referencedkeys(rdbms_referencedKeys rdbms_referencedkeys) {
        this.rdbms_referencedkeys = rdbms_referencedkeys;
    }

}