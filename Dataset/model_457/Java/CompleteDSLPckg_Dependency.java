





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Dependency extends DirectedRelationship, PackageableElement {






    private List<CompleteDSLPckg_NamedElement> completedslpckg_namedelements;




    private CompleteDSLPckg_CollaborationUse completedslpckg_collaborationuse;




    private List<CompleteDSLPckg_NamedElement> completedslpckg_namedelements;




    private CompleteDSLPckg_NamedElement completedslpckg_namedelement;


    public CompleteDSLPckg_Dependency(
    ) {
        super(
        );
        this.completedslpckg_namedelements = new ArrayList<>();
        this.completedslpckg_namedelements = new ArrayList<>();
    }

    public CompleteDSLPckg_Dependency(
        ArrayList<CompleteDSLPckg_NamedElement> completedslpckg_namedelements,        ArrayList<CompleteDSLPckg_NamedElement> completedslpckg_namedelements    ) {
        this.completedslpckg_namedelements = completedslpckg_namedelements;
        this.completedslpckg_namedelements = completedslpckg_namedelements;
    }


    public List<CompleteDSLPckg_NamedElement> getCompletedslpckg_namedelements() {
        return completedslpckg_namedelements;
    }

    public void addCompletedslpckg_namedelement(Completedslpckg_namedelement completedslpckg_namedelement) {
        this.completedslpckg_namedelements.add(completedslpckg_namedelement);
    }
    public CompleteDSLPckg_CollaborationUse getCompletedslpckg_collaborationuse() {
        return completedslpckg_collaborationuse;
    }

    public void setCompletedslpckg_collaborationuse(CompleteDSLPckg_CollaborationUse completedslpckg_collaborationuse) {
        this.completedslpckg_collaborationuse = completedslpckg_collaborationuse;
    }
    public List<CompleteDSLPckg_NamedElement> getCompletedslpckg_namedelements() {
        return completedslpckg_namedelements;
    }

    public void addCompletedslpckg_namedelement(Completedslpckg_namedelement completedslpckg_namedelement) {
        this.completedslpckg_namedelements.add(completedslpckg_namedelement);
    }
    public CompleteDSLPckg_NamedElement getCompletedslpckg_namedelement() {
        return completedslpckg_namedelement;
    }

    public void setCompletedslpckg_namedelement(CompleteDSLPckg_NamedElement completedslpckg_namedelement) {
        this.completedslpckg_namedelement = completedslpckg_namedelement;
    }

}