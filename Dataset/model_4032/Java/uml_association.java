





import java.util.List;
import java.util.ArrayList;

public class uml_association  {

    private String kind;
    private String oID;
    private String source;
    private String name;
    private String destination;



    public uml_association(
        String kind,        String oID,        String source,        String name,        String destination    ) {
        this.kind = kind;
        this.oID = oID;
        this.source = source;
        this.name = name;
        this.destination = destination;
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
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }


}