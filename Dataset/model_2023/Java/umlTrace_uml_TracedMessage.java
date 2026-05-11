





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedMessage extends TracedNamedElement {






    private uml_TracedInteraction uml_tracedinteraction;




    private uml_TracedConnector uml_tracedconnector;




    private uml_TracedNamedElement uml_tracednamedelement;




    private List<uml_TracedValueSpecification> uml_tracedvaluespecifications;


    public umlTrace_uml_TracedMessage(
    ) {
        super(
        );
        this.uml_tracedvaluespecifications = new ArrayList<>();
    }

    public umlTrace_uml_TracedMessage(
        ArrayList<uml_TracedValueSpecification> uml_tracedvaluespecifications    ) {
        this.uml_tracedvaluespecifications = uml_tracedvaluespecifications;
    }


    public uml_TracedInteraction getUml_tracedinteraction() {
        return uml_tracedinteraction;
    }

    public void setUml_tracedinteraction(uml_TracedInteraction uml_tracedinteraction) {
        this.uml_tracedinteraction = uml_tracedinteraction;
    }
    public uml_TracedConnector getUml_tracedconnector() {
        return uml_tracedconnector;
    }

    public void setUml_tracedconnector(uml_TracedConnector uml_tracedconnector) {
        this.uml_tracedconnector = uml_tracedconnector;
    }
    public uml_TracedNamedElement getUml_tracednamedelement() {
        return uml_tracednamedelement;
    }

    public void setUml_tracednamedelement(uml_TracedNamedElement uml_tracednamedelement) {
        this.uml_tracednamedelement = uml_tracednamedelement;
    }
    public List<uml_TracedValueSpecification> getUml_tracedvaluespecifications() {
        return uml_tracedvaluespecifications;
    }

    public void addUml_tracedvaluespecification(Uml_tracedvaluespecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecifications.add(uml_tracedvaluespecification);
    }

}