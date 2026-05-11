





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedCollaboration extends uml_TracedStructuredClassifier, uml_TracedBehavioredClassifier {






    private List<uml_TracedConnectableElement> uml_tracedconnectableelements;


    public umlTrace_uml_TracedCollaboration(
    ) {
        super(
        );
        this.uml_tracedconnectableelements = new ArrayList<>();
    }

    public umlTrace_uml_TracedCollaboration(
        ArrayList<uml_TracedConnectableElement> uml_tracedconnectableelements    ) {
        this.uml_tracedconnectableelements = uml_tracedconnectableelements;
    }


    public List<uml_TracedConnectableElement> getUml_tracedconnectableelements() {
        return uml_tracedconnectableelements;
    }

    public void addUml_tracedconnectableelement(Uml_tracedconnectableelement uml_tracedconnectableelement) {
        this.uml_tracedconnectableelements.add(uml_tracedconnectableelement);
    }

}