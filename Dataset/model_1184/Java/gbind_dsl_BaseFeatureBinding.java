





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_BaseFeatureBinding extends ConceptBinding {

    private String conceptFeature;



    public gbind_dsl_BaseFeatureBinding(
        String conceptFeature    ) {
        super(
        );
        this.conceptFeature = conceptFeature;
    }


    public String getConceptfeature() {
        return conceptFeature;
    }

    public void setConceptfeature(String conceptFeature) {
        this.conceptFeature = conceptFeature;
    }


}