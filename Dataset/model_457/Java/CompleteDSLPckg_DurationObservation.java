





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_DurationObservation extends Observation {

    private boolean firstEvent;





    private List<CompleteDSLPckg_NamedElement> completedslpckg_namedelements;


    public CompleteDSLPckg_DurationObservation(
        boolean firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
        this.completedslpckg_namedelements = new ArrayList<>();
    }

    public CompleteDSLPckg_DurationObservation(
        boolean firstEvent        ArrayList<CompleteDSLPckg_NamedElement> completedslpckg_namedelements    ) {
        this.firstEvent = firstEvent;
        this.completedslpckg_namedelements = completedslpckg_namedelements;
    }

    public boolean getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(boolean firstEvent) {
        this.firstEvent = firstEvent;
    }

    public List<CompleteDSLPckg_NamedElement> getCompletedslpckg_namedelements() {
        return completedslpckg_namedelements;
    }

    public void addCompletedslpckg_namedelement(Completedslpckg_namedelement completedslpckg_namedelement) {
        this.completedslpckg_namedelements.add(completedslpckg_namedelement);
    }

}