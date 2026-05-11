





import java.util.List;
import java.util.ArrayList;

public class aggregator_CustomCategory extends InfosProvider, StatusProvider {

    private String label;
    private String description;
    private String identifier;



    public aggregator_CustomCategory(
        String label,        String description,        String identifier    ) {
        super(
        );
        this.label = label;
        this.description = description;
        this.identifier = identifier;
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
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}