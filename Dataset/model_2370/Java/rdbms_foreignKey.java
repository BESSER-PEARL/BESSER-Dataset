





import java.util.List;
import java.util.ArrayList;

public class rdbms_foreignKey  {

    private String oID;
    private String refersTo;
    private String name;
    private String kind;
    private String owner;





    private rdbms_DocumentRoot rdbms_documentroot;


    public rdbms_foreignKey(
        String oID,        String refersTo,        String name,        String kind,        String owner    ) {
        this.oID = oID;
        this.refersTo = refersTo;
        this.name = name;
        this.kind = kind;
        this.owner = owner;
    }


    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }
    public String getRefersto() {
        return refersTo;
    }

    public void setRefersto(String refersTo) {
        this.refersTo = refersTo;
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
    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public rdbms_DocumentRoot getRdbms_documentroot() {
        return rdbms_documentroot;
    }

    public void setRdbms_documentroot(rdbms_DocumentRoot rdbms_documentroot) {
        this.rdbms_documentroot = rdbms_documentroot;
    }

}