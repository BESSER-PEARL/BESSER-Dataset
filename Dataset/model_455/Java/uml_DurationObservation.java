





import java.util.List;
import java.util.ArrayList;

public class uml_DurationObservation extends Observation {

    private String firstEvent;





    private List<uml_NamedElement> uml_namedelements;


    public uml_DurationObservation(
        String firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
        this.uml_namedelements = new ArrayList<>();
    }

    public uml_DurationObservation(
        String firstEvent        ArrayList<uml_NamedElement> uml_namedelements    ) {
        this.firstEvent = firstEvent;
        this.uml_namedelements = uml_namedelements;
    }

    public String getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(String firstEvent) {
        this.firstEvent = firstEvent;
    }

    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }

}