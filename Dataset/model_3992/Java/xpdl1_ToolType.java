





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ToolType  {

    private String description;
    private String type;
    private String id;





    private xpdl1_DocumentRoot xpdl1_documentroot;




    private xpdl1_ActualParametersType xpdl1_actualparameterstype;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;




    private xpdl1_ImplementationType xpdl1_implementationtype;


    public xpdl1_ToolType(
        String description,        String type,        String id    ) {
        this.description = description;
        this.type = type;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public xpdl1_ActualParametersType getXpdl1_actualparameterstype() {
        return xpdl1_actualparameterstype;
    }

    public void setXpdl1_actualparameterstype(xpdl1_ActualParametersType xpdl1_actualparameterstype) {
        this.xpdl1_actualparameterstype = xpdl1_actualparameterstype;
    }
    public xpdl1_ExtendedAttributesType getXpdl1_extendedattributestype() {
        return xpdl1_extendedattributestype;
    }

    public void setXpdl1_extendedattributestype(xpdl1_ExtendedAttributesType xpdl1_extendedattributestype) {
        this.xpdl1_extendedattributestype = xpdl1_extendedattributestype;
    }
    public xpdl1_ImplementationType getXpdl1_implementationtype() {
        return xpdl1_implementationtype;
    }

    public void setXpdl1_implementationtype(xpdl1_ImplementationType xpdl1_implementationtype) {
        this.xpdl1_implementationtype = xpdl1_implementationtype;
    }

}