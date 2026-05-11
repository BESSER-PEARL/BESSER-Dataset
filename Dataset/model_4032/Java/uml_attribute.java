





import java.util.List;
import java.util.ArrayList;

public class uml_attribute  {

    private String kind;
    private String oID;
    private String name;



    public uml_attribute(
        String kind,        String oID,        String name    ) {
        this.kind = kind;
        this.oID = oID;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}