





import java.util.List;
import java.util.ArrayList;

public class ConceptASE_IndividualContainer  {






    private List<ConceptASE_Thing> conceptase_things;


    public ConceptASE_IndividualContainer(
    ) {
        this.conceptase_things = new ArrayList<>();
    }

    public ConceptASE_IndividualContainer(
        ArrayList<ConceptASE_Thing> conceptase_things    ) {
        this.conceptase_things = conceptase_things;
    }


    public List<ConceptASE_Thing> getConceptase_things() {
        return conceptase_things;
    }

    public void addConceptase_thing(Conceptase_thing conceptase_thing) {
        this.conceptase_things.add(conceptase_thing);
    }

}