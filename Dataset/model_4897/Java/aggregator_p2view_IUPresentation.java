





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentation  {

    private String version;
    private String description;
    private String filter;
    private String name;
    private String label;
    private String type;
    private String id;



    public aggregator_p2view_IUPresentation(
        String version,        String description,        String filter,        String name,        String label,        String type,        String id    ) {
        this.version = version;
        this.description = description;
        this.filter = filter;
        this.name = name;
        this.label = label;
        this.type = type;
        this.id = id;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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


}