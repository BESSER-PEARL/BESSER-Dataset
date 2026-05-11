





import java.util.List;
import java.util.ArrayList;

public class rdbms_column  {

    private String oID;
    private String type;
    private String kind;
    private String name;



    public rdbms_column(
        String oID,        String type,        String kind,        String name    ) {
        this.oID = oID;
        this.type = type;
        this.kind = kind;
        this.name = name;
    }


    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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


}