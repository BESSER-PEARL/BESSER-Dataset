





import java.util.List;
import java.util.ArrayList;

public class aggregator_CustomCategory extends InfosProvider, StatusProvider {

    private String description;
    private String label;
    private String identifier;



    public aggregator_CustomCategory(
        String description,        String label,        String identifier    ) {
        super(
        );
        this.description = description;
        this.label = label;
        this.identifier = identifier;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}