





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedConnectableElement extends uml_TracedTypedElement, uml_TracedParameterableElement {






    private List<uml_TracedConnectorEnd> uml_tracedconnectorends;


    public umlTrace_uml_TracedConnectableElement(
    ) {
        super(
        );
        this.uml_tracedconnectorends = new ArrayList<>();
    }

    public umlTrace_uml_TracedConnectableElement(
        ArrayList<uml_TracedConnectorEnd> uml_tracedconnectorends    ) {
        this.uml_tracedconnectorends = uml_tracedconnectorends;
    }


    public List<uml_TracedConnectorEnd> getUml_tracedconnectorends() {
        return uml_tracedconnectorends;
    }

    public void addUml_tracedconnectorend(Uml_tracedconnectorend uml_tracedconnectorend) {
        this.uml_tracedconnectorends.add(uml_tracedconnectorend);
    }

}