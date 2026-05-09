





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Collaboration extends StructuredClassifier, BehavioredClassifier {






    private uml3_0_0_CollaborationUse uml3_0_0_collaborationuse;




    private List<uml3_0_0_ConnectableElement> uml3_0_0_connectableelements;


    public uml3_0_0_Collaboration(
    ) {
        super(
        );
        this.uml3_0_0_connectableelements = new ArrayList<>();
    }

    public uml3_0_0_Collaboration(
        ArrayList<uml3_0_0_ConnectableElement> uml3_0_0_connectableelements    ) {
        this.uml3_0_0_connectableelements = uml3_0_0_connectableelements;
    }


    public uml3_0_0_CollaborationUse getUml3_0_0_collaborationuse() {
        return uml3_0_0_collaborationuse;
    }

    public void setUml3_0_0_collaborationuse(uml3_0_0_CollaborationUse uml3_0_0_collaborationuse) {
        this.uml3_0_0_collaborationuse = uml3_0_0_collaborationuse;
    }
    public List<uml3_0_0_ConnectableElement> getUml3_0_0_connectableelements() {
        return uml3_0_0_connectableelements;
    }

    public void addUml3_0_0_connectableelement(Uml3_0_0_connectableelement uml3_0_0_connectableelement) {
        this.uml3_0_0_connectableelements.add(uml3_0_0_connectableelement);
    }

}