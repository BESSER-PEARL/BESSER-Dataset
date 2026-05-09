





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_DurationObservation extends Observation {

    private String firstEvent;





    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;


    public uml3_0_0_DurationObservation(
        String firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
        this.uml3_0_0_namedelements = new ArrayList<>();
    }

    public uml3_0_0_DurationObservation(
        String firstEvent        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements    ) {
        this.firstEvent = firstEvent;
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
    }

    public String getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(String firstEvent) {
        this.firstEvent = firstEvent;
    }

    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }

}