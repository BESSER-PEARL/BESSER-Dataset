





import java.util.List;
import java.util.ArrayList;

public class diagram_description_CustomLayoutConfiguration extends Layout {

    private String label;
    private String description;
    private String id;



    public diagram_description_CustomLayoutConfiguration(
        String label,        String description,        String id    ) {
        super(
        );
        this.label = label;
        this.description = description;
        this.id = id;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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


}