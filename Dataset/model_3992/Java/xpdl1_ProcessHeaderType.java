





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ProcessHeaderType  {

    private String validTo;
    private String description;
    private String limit;
    private String created;
    private String priority;
    private String validFrom;
    private String durationUnit;





    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_ProcessHeaderType(
        String validTo,        String description,        String limit,        String created,        String priority,        String validFrom,        String durationUnit    ) {
        this.validTo = validTo;
        this.description = description;
        this.limit = limit;
        this.created = created;
        this.priority = priority;
        this.validFrom = validFrom;
        this.durationUnit = durationUnit;
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
    public String getLimit() {
        return limit;
    }

    public void setLimit(String limit) {
        this.limit = limit;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getValidfrom() {
        return validFrom;
    }

    public void setValidfrom(String validFrom) {
        this.validFrom = validFrom;
    }
    public String getDurationunit() {
        return durationUnit;
    }

    public void setDurationunit(String durationUnit) {
        this.durationUnit = durationUnit;
    }

    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}