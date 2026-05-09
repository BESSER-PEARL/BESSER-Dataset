





import java.util.List;
import java.util.ArrayList;

public class uml_Collaboration extends StructuredClassifier, BehavioredClassifier {






    private List<uml_ConnectableElement> uml_connectableelements;




    private uml_CollaborationUse uml_collaborationuse;


    public uml_Collaboration(
    ) {
        super(
        );
        this.uml_connectableelements = new ArrayList<>();
    }

    public uml_Collaboration(
        ArrayList<uml_ConnectableElement> uml_connectableelements    ) {
        this.uml_connectableelements = uml_connectableelements;
    }


    public List<uml_ConnectableElement> getUml_connectableelements() {
        return uml_connectableelements;
    }

    public void addUml_connectableelement(Uml_connectableelement uml_connectableelement) {
        this.uml_connectableelements.add(uml_connectableelement);
    }
    public uml_CollaborationUse getUml_collaborationuse() {
        return uml_collaborationuse;
    }

    public void setUml_collaborationuse(uml_CollaborationUse uml_collaborationuse) {
        this.uml_collaborationuse = uml_collaborationuse;
    }

}