





import java.util.List;
import java.util.ArrayList;

public class xpdl_ExternalReferenceType extends XpdlTypeType {

    private String xref;
    private String namespace;
    private String location;



    public xpdl_ExternalReferenceType(
        String xref,        String namespace,        String location    ) {
        super(
        );
        this.xref = xref;
        this.namespace = namespace;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}