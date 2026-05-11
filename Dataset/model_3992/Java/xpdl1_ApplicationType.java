





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ApplicationType  {

    private String id;
    private String name;
    private String description;





    private xpdl1_ExternalReferenceType xpdl1_externalreferencetype;




    private xpdl1_FormalParametersType xpdl1_formalparameterstype;




    private xpdl1_ApplicationsType xpdl1_applicationstype;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;


    public xpdl1_ApplicationType(
        String id,        String name,        String description    ) {
        this.id = id;
        this.name = name;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public xpdl1_ExternalReferenceType getXpdl1_externalreferencetype() {
        return xpdl1_externalreferencetype;
    }

    public void setXpdl1_externalreferencetype(xpdl1_ExternalReferenceType xpdl1_externalreferencetype) {
        this.xpdl1_externalreferencetype = xpdl1_externalreferencetype;
    }
    public xpdl1_FormalParametersType getXpdl1_formalparameterstype() {
        return xpdl1_formalparameterstype;
    }

    public void setXpdl1_formalparameterstype(xpdl1_FormalParametersType xpdl1_formalparameterstype) {
        this.xpdl1_formalparameterstype = xpdl1_formalparameterstype;
    }
    public xpdl1_ApplicationsType getXpdl1_applicationstype() {
        return xpdl1_applicationstype;
    }

    public void setXpdl1_applicationstype(xpdl1_ApplicationsType xpdl1_applicationstype) {
        this.xpdl1_applicationstype = xpdl1_applicationstype;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }

}