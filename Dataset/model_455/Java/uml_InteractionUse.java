





import java.util.List;
import java.util.ArrayList;

public class uml_InteractionUse extends InteractionFragment {






    private List<uml_Action> uml_actions;




    private List<uml_Gate> uml_gates;




    private uml_Interaction uml_interaction;


    public uml_InteractionUse(
    ) {
        super(
        );
        this.uml_actions = new ArrayList<>();
        this.uml_gates = new ArrayList<>();
    }

    public uml_InteractionUse(
        ArrayList<uml_Action> uml_actions,        ArrayList<uml_Gate> uml_gates    ) {
        this.uml_actions = uml_actions;
        this.uml_gates = uml_gates;
    }


    public List<uml_Action> getUml_actions() {
        return uml_actions;
    }

    public void addUml_action(Uml_action uml_action) {
        this.uml_actions.add(uml_action);
    }
    public List<uml_Gate> getUml_gates() {
        return uml_gates;
    }

    public void addUml_gate(Uml_gate uml_gate) {
        this.uml_gates.add(uml_gate);
    }
    public uml_Interaction getUml_interaction() {
        return uml_interaction;
    }

    public void setUml_interaction(uml_Interaction uml_interaction) {
        this.uml_interaction = uml_interaction;
    }

}