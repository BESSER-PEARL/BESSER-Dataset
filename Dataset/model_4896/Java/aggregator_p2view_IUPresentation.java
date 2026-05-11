





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentation  {

    private String id;
    private String name;
    private String filter;
    private String description;
    private String type;
    private String label;
    private String version;



    public aggregator_p2view_IUPresentation(
        String id,        String name,        String filter,        String description,        String type,        String label,        String version    ) {
        this.id = id;
        this.name = name;
        this.filter = filter;
        this.description = description;
        this.type = type;
        this.label = label;
        this.version = version;
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
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}