





import java.util.List;
import java.util.ArrayList;

public class Concept_Sensor extends Thing {






    private List<Concept_Trackelement> concept_trackelements;




    private Concept_Trackelement concept_trackelement;


    public Concept_Sensor(
    ) {
        super(
        );
        this.concept_trackelements = new ArrayList<>();
    }

    public Concept_Sensor(
        ArrayList<Concept_Trackelement> concept_trackelements    ) {
        this.concept_trackelements = concept_trackelements;
    }


    public List<Concept_Trackelement> getConcept_trackelements() {
        return concept_trackelements;
    }

    public void addConcept_trackelement(Concept_trackelement concept_trackelement) {
        this.concept_trackelements.add(concept_trackelement);
    }
    public Concept_Trackelement getConcept_trackelement() {
        return concept_trackelement;
    }

    public void setConcept_trackelement(Concept_Trackelement concept_trackelement) {
        this.concept_trackelement = concept_trackelement;
    }

}