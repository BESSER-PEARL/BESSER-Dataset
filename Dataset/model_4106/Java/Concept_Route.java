





import java.util.List;
import java.util.ArrayList;

public class Concept_Route extends Thing {






    private Concept_Signal concept_signal;




    private Concept_Signal concept_signal;




    private List<Concept_Sensor> concept_sensors;


    public Concept_Route(
    ) {
        super(
        );
        this.concept_sensors = new ArrayList<>();
    }

    public Concept_Route(
        ArrayList<Concept_Sensor> concept_sensors    ) {
        this.concept_sensors = concept_sensors;
    }


    public Concept_Signal getConcept_signal() {
        return concept_signal;
    }

    public void setConcept_signal(Concept_Signal concept_signal) {
        this.concept_signal = concept_signal;
    }
    public Concept_Signal getConcept_signal() {
        return concept_signal;
    }

    public void setConcept_signal(Concept_Signal concept_signal) {
        this.concept_signal = concept_signal;
    }
    public List<Concept_Sensor> getConcept_sensors() {
        return concept_sensors;
    }

    public void addConcept_sensor(Concept_sensor concept_sensor) {
        this.concept_sensors.add(concept_sensor);
    }

}