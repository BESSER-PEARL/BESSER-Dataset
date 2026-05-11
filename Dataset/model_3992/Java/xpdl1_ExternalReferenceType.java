





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ExternalReferenceType  {

    private String location;
    private String xref;
    private String namespace;



    public xpdl1_ExternalReferenceType(
        String location,        String xref,        String namespace    ) {
        this.location = location;
        this.xref = xref;
        this.namespace = namespace;
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


}