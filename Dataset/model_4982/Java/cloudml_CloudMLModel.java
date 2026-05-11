





import java.util.List;
import java.util.ArrayList;

public class cloudml_CloudMLModel extends CloudMLElementWithProperties {






    private List<cloudml_RelationshipInstance> cloudml_relationshipinstances;


    public cloudml_CloudMLModel(
    ) {
        super(
        );
        this.cloudml_relationshipinstances = new ArrayList<>();
    }

    public cloudml_CloudMLModel(
        ArrayList<cloudml_RelationshipInstance> cloudml_relationshipinstances    ) {
        this.cloudml_relationshipinstances = cloudml_relationshipinstances;
    }


    public List<cloudml_RelationshipInstance> getCloudml_relationshipinstances() {
        return cloudml_relationshipinstances;
    }

    public void addCloudml_relationshipinstance(Cloudml_relationshipinstance cloudml_relationshipinstance) {
        this.cloudml_relationshipinstances.add(cloudml_relationshipinstance);
    }

}