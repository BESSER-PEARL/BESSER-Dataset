





import java.util.List;
import java.util.ArrayList;

public class xpdl_ExternalReferenceType extends XpdlTypeType {

    private String location;
    private String xref;
    private String namespace;





    private xpdl_DataTypeType xpdl_datatypetype;


    public xpdl_ExternalReferenceType(
        String location,        String xref,        String namespace    ) {
        super(
        );
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

    public xpdl_DataTypeType getXpdl_datatypetype() {
        return xpdl_datatypetype;
    }

    public void setXpdl_datatypetype(xpdl_DataTypeType xpdl_datatypetype) {
        this.xpdl_datatypetype = xpdl_datatypetype;
    }

}