





import java.util.List;
import java.util.ArrayList;

public class rdbms_schema  {

    private String kind;
    private String name;
    private String oID;





    private rdbms_foreignKeys rdbms_foreignkeys;




    private rdbms_DocumentRoot rdbms_documentroot;


    public rdbms_schema(
        String kind,        String name,        String oID    ) {
        this.kind = kind;
        this.name = name;
        this.oID = oID;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }

    public rdbms_foreignKeys getRdbms_foreignkeys() {
        return rdbms_foreignkeys;
    }

    public void setRdbms_foreignkeys(rdbms_foreignKeys rdbms_foreignkeys) {
        this.rdbms_foreignkeys = rdbms_foreignkeys;
    }
    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }

}