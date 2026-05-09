





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_TimeObservation extends Observation {

    private boolean firstEvent;





    private CompleteDSLPckg_NamedElement completedslpckg_namedelement;


    public CompleteDSLPckg_TimeObservation(
        boolean firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
    }


    public boolean getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(boolean firstEvent) {
        this.firstEvent = firstEvent;
    }

    public CompleteDSLPckg_NamedElement getCompletedslpckg_namedelement() {
        return completedslpckg_namedelement;
    }

    public void setCompletedslpckg_namedelement(CompleteDSLPckg_NamedElement completedslpckg_namedelement) {
        this.completedslpckg_namedelement = completedslpckg_namedelement;
    }

}