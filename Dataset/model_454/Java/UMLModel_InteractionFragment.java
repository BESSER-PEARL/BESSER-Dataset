





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InteractionFragment extends NamedElement {

    private String enclosingOperand;
    private String covered;
    private String enclosingInteraction;





    private UMLModel_Interaction umlmodel_interaction;




    private List<UMLModel_GeneralOrdering> umlmodel_generalorderings;


    public UMLModel_InteractionFragment(
        String enclosingOperand,        String covered,        String enclosingInteraction    ) {
        super(
        );
        this.enclosingOperand = enclosingOperand;
        this.covered = covered;
        this.enclosingInteraction = enclosingInteraction;
        this.umlmodel_generalorderings = new ArrayList<>();
    }

    public UMLModel_InteractionFragment(
        String enclosingOperand,        String covered,        String enclosingInteraction        ArrayList<UMLModel_GeneralOrdering> umlmodel_generalorderings    ) {
        this.enclosingOperand = enclosingOperand;
        this.covered = covered;
        this.enclosingInteraction = enclosingInteraction;
        this.umlmodel_generalorderings = umlmodel_generalorderings;
    }

    public String getEnclosingoperand() {
        return enclosingOperand;
    }

    public void setEnclosingoperand(String enclosingOperand) {
        this.enclosingOperand = enclosingOperand;
    }
    public String getCovered() {
        return covered;
    }

    public void setCovered(String covered) {
        this.covered = covered;
    }
    public String getEnclosinginteraction() {
        return enclosingInteraction;
    }

    public void setEnclosinginteraction(String enclosingInteraction) {
        this.enclosingInteraction = enclosingInteraction;
    }

    public UMLModel_Interaction getUmlmodel_interaction() {
        return umlmodel_interaction;
    }

    public void setUmlmodel_interaction(UMLModel_Interaction umlmodel_interaction) {
        this.umlmodel_interaction = umlmodel_interaction;
    }
    public List<UMLModel_GeneralOrdering> getUmlmodel_generalorderings() {
        return umlmodel_generalorderings;
    }

    public void addUmlmodel_generalordering(Umlmodel_generalordering umlmodel_generalordering) {
        this.umlmodel_generalorderings.add(umlmodel_generalordering);
    }

}