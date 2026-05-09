





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Collaboration extends StructuredClassifier, BehavioredClassifier {






    private CompleteDSLPckg_CollaborationUse completedslpckg_collaborationuse;




    private List<CompleteDSLPckg_ConnectableElement> completedslpckg_connectableelements;


    public CompleteDSLPckg_Collaboration(
    ) {
        super(
        );
        this.completedslpckg_connectableelements = new ArrayList<>();
    }

    public CompleteDSLPckg_Collaboration(
        ArrayList<CompleteDSLPckg_ConnectableElement> completedslpckg_connectableelements    ) {
        this.completedslpckg_connectableelements = completedslpckg_connectableelements;
    }


    public CompleteDSLPckg_CollaborationUse getCompletedslpckg_collaborationuse() {
        return completedslpckg_collaborationuse;
    }

    public void setCompletedslpckg_collaborationuse(CompleteDSLPckg_CollaborationUse completedslpckg_collaborationuse) {
        this.completedslpckg_collaborationuse = completedslpckg_collaborationuse;
    }
    public List<CompleteDSLPckg_ConnectableElement> getCompletedslpckg_connectableelements() {
        return completedslpckg_connectableelements;
    }

    public void addCompletedslpckg_connectableelement(Completedslpckg_connectableelement completedslpckg_connectableelement) {
        this.completedslpckg_connectableelements.add(completedslpckg_connectableelement);
    }

}