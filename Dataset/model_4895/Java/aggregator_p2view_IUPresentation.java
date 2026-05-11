





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2view_IUPresentation  {

    private String type;
    private String id;
    private String description;
    private String name;
    private String version;
    private String label;
    private String filter;



    public aggregator_p2view_IUPresentation(
        String type,        String id,        String description,        String name,        String version,        String label,        String filter    ) {
        this.type = type;
        this.id = id;
        this.description = description;
        this.name = name;
        this.version = version;
        this.label = label;
        this.filter = filter;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }


}