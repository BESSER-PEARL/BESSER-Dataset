





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_TimeObservation extends Observation {

    private String firstEvent;





    private uml3_0_0_NamedElement uml3_0_0_namedelement;


    public uml3_0_0_TimeObservation(
        String firstEvent    ) {
        super(
        );
        this.firstEvent = firstEvent;
    }


    public String getFirstevent() {
        return firstEvent;
    }

    public void setFirstevent(String firstEvent) {
        this.firstEvent = firstEvent;
    }

    public uml3_0_0_NamedElement getUml3_0_0_namedelement() {
        return uml3_0_0_namedelement;
    }

    public void setUml3_0_0_namedelement(uml3_0_0_NamedElement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelement = uml3_0_0_namedelement;
    }

}