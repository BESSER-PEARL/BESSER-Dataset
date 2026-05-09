





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Collaboration extends StructuredClassifier, BehavioredClassifier {






    private UML2WithID_CollaborationOccurrence uml2withid_collaborationoccurrence;




    private List<UML2WithID_ConnectableElement> uml2withid_connectableelements;


    public UML2WithID_Collaboration(
    ) {
        super(
        );
        this.uml2withid_connectableelements = new ArrayList<>();
    }

    public UML2WithID_Collaboration(
        ArrayList<UML2WithID_ConnectableElement> uml2withid_connectableelements    ) {
        this.uml2withid_connectableelements = uml2withid_connectableelements;
    }


    public UML2WithID_CollaborationOccurrence getUml2withid_collaborationoccurrence() {
        return uml2withid_collaborationoccurrence;
    }

    public void setUml2withid_collaborationoccurrence(UML2WithID_CollaborationOccurrence uml2withid_collaborationoccurrence) {
        this.uml2withid_collaborationoccurrence = uml2withid_collaborationoccurrence;
    }
    public List<UML2WithID_ConnectableElement> getUml2withid_connectableelements() {
        return uml2withid_connectableelements;
    }

    public void addUml2withid_connectableelement(Uml2withid_connectableelement uml2withid_connectableelement) {
        this.uml2withid_connectableelements.add(uml2withid_connectableelement);
    }

}