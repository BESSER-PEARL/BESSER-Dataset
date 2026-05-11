





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ExternalReferenceType  {

    private String namespace;
    private String xref;
    private String location;





    private xpdl1_ArrayTypeType xpdl1_arraytypetype;




    private xpdl1_ApplicationType xpdl1_applicationtype;


    public xpdl1_ExternalReferenceType(
        String namespace,        String xref,        String location    ) {
        this.namespace = namespace;
        this.xref = xref;
        this.location = location;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getXref() {
        return xref;
    }

    public void setXref(String xref) {
        this.xref = xref;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public xpdl1_ArrayTypeType getXpdl1_arraytypetype() {
        return xpdl1_arraytypetype;
    }

    public void setXpdl1_arraytypetype(xpdl1_ArrayTypeType xpdl1_arraytypetype) {
        this.xpdl1_arraytypetype = xpdl1_arraytypetype;
    }
    public xpdl1_ApplicationType getXpdl1_applicationtype() {
        return xpdl1_applicationtype;
    }

    public void setXpdl1_applicationtype(xpdl1_ApplicationType xpdl1_applicationtype) {
        this.xpdl1_applicationtype = xpdl1_applicationtype;
    }

}