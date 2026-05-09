





import java.util.List;
import java.util.ArrayList;

public class gbind_dsl_VirtualClassBinding extends ConceptBinding {






    private List<ConceptFeatureRef> conceptfeaturerefs;


    public gbind_dsl_VirtualClassBinding(
    ) {
        super(
        );
        this.conceptfeaturerefs = new ArrayList<>();
    }

    public gbind_dsl_VirtualClassBinding(
        ArrayList<ConceptFeatureRef> conceptfeaturerefs    ) {
        this.conceptfeaturerefs = conceptfeaturerefs;
    }


    public List<ConceptFeatureRef> getConceptfeaturerefs() {
        return conceptfeaturerefs;
    }

    public void addConceptfeatureref(Conceptfeatureref conceptfeatureref) {
        this.conceptfeaturerefs.add(conceptfeatureref);
    }

}