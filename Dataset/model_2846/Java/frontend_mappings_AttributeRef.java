





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_AttributeRef extends MetamodelElementRef {

    private String featureName;
    private boolean multivalued;





    private MatchedElement matchedelement;


    public frontend_mappings_AttributeRef(
        String featureName,        boolean multivalued    ) {
        super(
        );
        this.featureName = featureName;
        this.multivalued = multivalued;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }

    public MatchedElement getMatchedelement() {
        return matchedelement;
    }

    public void setMatchedelement(MatchedElement matchedelement) {
        this.matchedelement = matchedelement;
    }

}