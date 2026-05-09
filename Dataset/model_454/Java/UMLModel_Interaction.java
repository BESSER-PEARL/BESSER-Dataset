





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Interaction extends InteractionFragment, Behavior {






    private List<UMLModel_Gate> umlmodel_gates;




    private List<UMLModel_Action> umlmodel_actions;


    public UMLModel_Interaction(
    ) {
        super(
        );
        this.umlmodel_gates = new ArrayList<>();
        this.umlmodel_actions = new ArrayList<>();
    }

    public UMLModel_Interaction(
        ArrayList<UMLModel_Gate> umlmodel_gates,        ArrayList<UMLModel_Action> umlmodel_actions    ) {
        this.umlmodel_gates = umlmodel_gates;
        this.umlmodel_actions = umlmodel_actions;
    }


    public List<UMLModel_Gate> getUmlmodel_gates() {
        return umlmodel_gates;
    }

    public void addUmlmodel_gate(Umlmodel_gate umlmodel_gate) {
        this.umlmodel_gates.add(umlmodel_gate);
    }
    public List<UMLModel_Action> getUmlmodel_actions() {
        return umlmodel_actions;
    }

    public void addUmlmodel_action(Umlmodel_action umlmodel_action) {
        this.umlmodel_actions.add(umlmodel_action);
    }

}