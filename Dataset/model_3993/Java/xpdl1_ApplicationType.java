





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ApplicationType  {

    private String description;
    private String name;
    private String id;





    private xpdl1_ApplicationsType xpdl1_applicationstype;




    private xpdl1_ExtendedAttributesType xpdl1_extendedattributestype;


    public xpdl1_ApplicationType(
        String description,        String name,        String id    ) {
        this.description = description;
        this.name = name;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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