





import java.util.List;
import java.util.ArrayList;

public class ConceptASE_Route extends Thing {






    private List<ConceptASE_Sensor> conceptase_sensors;


    public ConceptASE_Route(
    ) {
        super(
        );
        this.conceptase_sensors = new ArrayList<>();
    }

    public ConceptASE_Route(
        ArrayList<ConceptASE_Sensor> conceptase_sensors    ) {
        this.conceptase_sensors = conceptase_sensors;
    }


    public List<ConceptASE_Sensor> getConceptase_sensors() {
        return conceptase_sensors;
    }

    public void addConceptase_sensor(Conceptase_sensor conceptase_sensor) {
        this.conceptase_sensors.add(conceptase_sensor);
    }

}