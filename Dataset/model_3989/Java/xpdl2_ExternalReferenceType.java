





import java.util.List;
import java.util.ArrayList;

public class xpdl2_ExternalReferenceType extends XpdlTypeType {

    private String location;
    private String xref;
    private String namespace;
    private String uuid;



    public xpdl2_ExternalReferenceType(
        String location,        String xref,        String namespace,        String uuid    ) {
        super(
        );
        this.location = location;
        this.xref = xref;
        this.namespace = namespace;
        this.uuid = uuid;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getXref() {
        return xref;
    }

    public void setXref(String xref) {
        this.xref = xref;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }


}