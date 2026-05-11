





import java.util.List;
import java.util.ArrayList;

public class xpdl1_PackageHeaderType  {

    private String costUnit;
    private String created;
    private String xPDLVersion;
    private String documentation;
    private String priorityUnit;
    private String description;
    private String vendor;





    private xpdl1_PackageType xpdl1_packagetype;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_PackageHeaderType(
        String costUnit,        String created,        String xPDLVersion,        String documentation,        String priorityUnit,        String description,        String vendor    ) {
        this.costUnit = costUnit;
        this.created = created;
        this.xPDLVersion = xPDLVersion;
        this.documentation = documentation;
        this.priorityUnit = priorityUnit;
        this.description = description;
        this.vendor = vendor;
    }


    public String getCostunit() {
        return costUnit;
    }

    public void setCostunit(String costUnit) {
        this.costUnit = costUnit;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getXpdlversion() {
        return xPDLVersion;
    }

    public void setXpdlversion(String xPDLVersion) {
        this.xPDLVersion = xPDLVersion;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getPriorityunit() {
        return priorityUnit;
    }

    public void setPriorityunit(String priorityUnit) {
        this.priorityUnit = priorityUnit;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }

    public xpdl1_PackageType getXpdl1_packagetype() {
        return xpdl1_packagetype;
    }

    public void setXpdl1_packagetype(xpdl1_PackageType xpdl1_packagetype) {
        this.xpdl1_packagetype = xpdl1_packagetype;
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}