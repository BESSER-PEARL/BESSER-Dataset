





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ActivityType  {

    private String name;
    private String description;
    private String id;
    private String documentation;
    private String icon;
    private String priority;
    private String performer;
    private String limit;





    private xpdl1_ActivitiesType xpdl1_activitiestype;


    public xpdl1_ActivityType(
        String name,        String description,        String id,        String documentation,        String icon,        String priority,        String performer,        String limit    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.documentation = documentation;
        this.icon = icon;
        this.priority = priority;
        this.performer = performer;
        this.limit = limit;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
    public String getPerformer() {
        return performer;
    }

    public void setPerformer(String performer) {
        this.performer = performer;
    }
    public String getLimit() {
        return limit;
    }

    public void setLimit(String limit) {
        this.limit = limit;
    }

    public xpdl1_ActivitiesType getXpdl1_activitiestype() {
        return xpdl1_activitiestype;
    }

    public void setXpdl1_activitiestype(xpdl1_ActivitiesType xpdl1_activitiestype) {
        this.xpdl1_activitiestype = xpdl1_activitiestype;
    }

}