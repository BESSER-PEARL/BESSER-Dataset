





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_AttributeRef extends MetamodelElementRef {

    private boolean multivalued;
    private String featureName;





    private MatchedElement matchedelement;


    public frontend_mappings_AttributeRef(
        boolean multivalued,        String featureName    ) {
        super(
        );
        this.multivalued = multivalued;
        this.featureName = featureName;
    }


    public boolean getMultivalued() {
        return multivalued;
    }

    public void setMultivalued(boolean multivalued) {
        this.multivalued = multivalued;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }

    public MatchedElement getMatchedelement() {
        return matchedelement;
    }

    public void setMatchedelement(MatchedElement matchedelement) {
        this.matchedelement = matchedelement;
    }

}