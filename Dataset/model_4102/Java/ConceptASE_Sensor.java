





import java.util.List;
import java.util.ArrayList;

public class ConceptASE_Sensor extends Thing {

    private int Sensor_year;





    private List<ConceptASE_Trackelement> conceptase_trackelements;




    private ConceptASE_Trackelement conceptase_trackelement;


    public ConceptASE_Sensor(
        int Sensor_year    ) {
        super(
        );
        this.Sensor_year = Sensor_year;
        this.conceptase_trackelements = new ArrayList<>();
    }

    public ConceptASE_Sensor(
        int Sensor_year        ArrayList<ConceptASE_Trackelement> conceptase_trackelements    ) {
        this.Sensor_year = Sensor_year;
        this.conceptase_trackelements = conceptase_trackelements;
    }

    public int getSensor_year() {
        return Sensor_year;
    }

    public void setSensor_year(int Sensor_year) {
        this.Sensor_year = Sensor_year;
    }

    public List<ConceptASE_Trackelement> getConceptase_trackelements() {
        return conceptase_trackelements;
    }

    public void addConceptase_trackelement(Conceptase_trackelement conceptase_trackelement) {
        this.conceptase_trackelements.add(conceptase_trackelement);
    }
    public ConceptASE_Trackelement getConceptase_trackelement() {
        return conceptase_trackelement;
    }

    public void setConceptase_trackelement(ConceptASE_Trackelement conceptase_trackelement) {
        this.conceptase_trackelement = conceptase_trackelement;
    }

}