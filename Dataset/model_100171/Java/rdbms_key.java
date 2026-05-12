





import java.util.List;
import java.util.ArrayList;

public class rdbms_key  {

    private String name;
    private String kind;
    private String oID;





    private rdbms_DocumentRoot rdbms_documentroot;


    public rdbms_key(
        String name,        String kind,        String oID    ) {
        this.name = name;
        this.kind = kind;
        this.oID = oID;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
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

}