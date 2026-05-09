





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InteractionUse extends InteractionFragment {

    private String refersTo;





    private List<UMLModel_Action> umlmodel_actions;




    private List<UMLModel_Gate> umlmodel_gates;


    public UMLModel_InteractionUse(
        String refersTo    ) {
        super(
        );
        this.refersTo = refersTo;
        this.umlmodel_actions = new ArrayList<>();
        this.umlmodel_gates = new ArrayList<>();
    }

    public UMLModel_InteractionUse(
        String refersTo        ArrayList<UMLModel_Action> umlmodel_actions,        ArrayList<UMLModel_Gate> umlmodel_gates    ) {
        this.refersTo = refersTo;
        this.umlmodel_actions = umlmodel_actions;
        this.umlmodel_gates = umlmodel_gates;
    }

    public String getRefersto() {
        return refersTo;
    }

    public void setRefersto(String refersTo) {
        this.refersTo = refersTo;
    }

    public List<UMLModel_Action> getUmlmodel_actions() {
        return umlmodel_actions;
    }

    public void addUmlmodel_action(Umlmodel_action umlmodel_action) {
        this.umlmodel_actions.add(umlmodel_action);
    }
    public List<UMLModel_Gate> getUmlmodel_gates() {
        return umlmodel_gates;
    }

    public void addUmlmodel_gate(Umlmodel_gate umlmodel_gate) {
        this.umlmodel_gates.add(umlmodel_gate);
    }

}