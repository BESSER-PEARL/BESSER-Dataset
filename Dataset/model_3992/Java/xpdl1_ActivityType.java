





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ActivityType  {

    private String name;
    private String performer;
    private String id;
    private String icon;
    private String limit;
    private String description;
    private String documentation;
    private String priority;



    public xpdl1_ActivityType(
        String name,        String performer,        String id,        String icon,        String limit,        String description,        String documentation,        String priority    ) {
        this.name = name;
        this.performer = performer;
        this.id = id;
        this.icon = icon;
        this.limit = limit;
        this.description = description;
        this.documentation = documentation;
        this.priority = priority;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPerformer() {
        return performer;
    }

    public void setPerformer(String performer) {
        this.performer = performer;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getLimit() {
        return limit;
    }

    public void setLimit(String limit) {
        this.limit = limit;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }
    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }


}