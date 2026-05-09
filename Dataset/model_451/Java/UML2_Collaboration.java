





import java.util.List;
import java.util.ArrayList;

public class UML2_Collaboration extends StructuredClassifier, BehavioredClassifier {






    private UML2_CollaborationOccurrence uml2_collaborationoccurrence;




    private List<UML2_ConnectableElement> uml2_connectableelements;


    public UML2_Collaboration(
    ) {
        super(
        );
        this.uml2_connectableelements = new ArrayList<>();
    }

    public UML2_Collaboration(
        ArrayList<UML2_ConnectableElement> uml2_connectableelements    ) {
        this.uml2_connectableelements = uml2_connectableelements;
    }


    public UML2_CollaborationOccurrence getUml2_collaborationoccurrence() {
        return uml2_collaborationoccurrence;
    }

    public void setUml2_collaborationoccurrence(UML2_CollaborationOccurrence uml2_collaborationoccurrence) {
        this.uml2_collaborationoccurrence = uml2_collaborationoccurrence;
    }
    public List<UML2_ConnectableElement> getUml2_connectableelements() {
        return uml2_connectableelements;
    }

    public void addUml2_connectableelement(Uml2_connectableelement uml2_connectableelement) {
        this.uml2_connectableelements.add(uml2_connectableelement);
    }

}