





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ProcessHeaderType  {

    private String validFrom;
    private String validTo;
    private String description;
    private String priority;
    private String durationUnit;
    private String created;
    private String limit;





    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_ProcessHeaderType(
        String validFrom,        String validTo,        String description,        String priority,        String durationUnit,        String created,        String limit    ) {
        this.validFrom = validFrom;
        this.validTo = validTo;
        this.description = description;
        this.priority = priority;
        this.durationUnit = durationUnit;
        this.created = created;
        this.limit = limit;
    }


    public String getValidfrom() {
        return validFrom;
    }

    public void setValidfrom(String validFrom) {
        this.validFrom = validFrom;
    }
    public String getValidto() {
        return validTo;
    }

    public void setValidto(String validTo) {
        this.validTo = validTo;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getDurationunit() {
        return durationUnit;
    }

    public void setDurationunit(String durationUnit) {
        this.durationUnit = durationUnit;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getLimit() {
        return limit;
    }

    public void setLimit(String limit) {
        this.limit = limit;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}