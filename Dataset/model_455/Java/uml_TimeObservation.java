





import java.util.List;
import java.util.ArrayList;

public class uml_TimeObservation extends Observation {

    private String firstEvent;





    private uml_NamedElement uml_namedelement;


    public uml_TimeObservation(
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

    public uml_NamedElement getUml_namedelement() {
        return uml_namedelement;
    }

    public void setUml_namedelement(uml_NamedElement uml_namedelement) {
        this.uml_namedelement = uml_namedelement;
    }

}