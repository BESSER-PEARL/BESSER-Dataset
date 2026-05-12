





import java.util.List;
import java.util.ArrayList;

public class rdbms_foreignKey  {

    private String refersTo;
    private String oID;
    private String owner;
    private String kind;
    private String name;





    private rdbms_DocumentRoot rdbms_documentroot;


    public rdbms_foreignKey(
        String refersTo,        String oID,        String owner,        String kind,        String name    ) {
        this.refersTo = refersTo;
        this.oID = oID;
        this.owner = owner;
        this.kind = kind;
        this.name = name;
    }


    public String getRefersto() {
        return refersTo;
    }

    public void setRefersto(String refersTo) {
        this.refersTo = refersTo;
    }
    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
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

    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }

}