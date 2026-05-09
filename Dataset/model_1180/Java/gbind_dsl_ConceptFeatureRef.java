





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_ConceptFeatureRef  {

    private String featureName;





    private ConceptMetaclass conceptmetaclass;


    public gbind_dsl_ConceptFeatureRef(
        String featureName    ) {
        this.featureName = featureName;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }

    public ConceptMetaclass getConceptmetaclass() {
        return conceptmetaclass;
    }

    public void setConceptmetaclass(ConceptMetaclass conceptmetaclass) {
        this.conceptmetaclass = conceptmetaclass;
    }

}