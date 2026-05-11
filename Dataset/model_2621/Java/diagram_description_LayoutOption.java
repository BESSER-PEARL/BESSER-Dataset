





import java.util.List;
import java.util.ArrayList;

public class diagram_description_LayoutOption  {

    private String id;
    private String description;
    private String targets;
    private String label;



    public diagram_description_LayoutOption(
        String id,        String description,        String targets,        String label    ) {
        this.id = id;
        this.description = description;
        this.targets = targets;
        this.label = label;
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
    public String getTargets() {
        return targets;
    }

    public void setTargets(String targets) {
        this.targets = targets;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}