





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_InteractionUse extends InteractionFragment {






    private List<uml3_0_0_Gate> uml3_0_0_gates;




    private uml3_0_0_Interaction uml3_0_0_interaction;


    public uml3_0_0_InteractionUse(
    ) {
        super(
        );
        this.uml3_0_0_gates = new ArrayList<>();
    }

    public uml3_0_0_InteractionUse(
        ArrayList<uml3_0_0_Gate> uml3_0_0_gates    ) {
        this.uml3_0_0_gates = uml3_0_0_gates;
    }


    public List<uml3_0_0_Gate> getUml3_0_0_gates() {
        return uml3_0_0_gates;
    }

    public void addUml3_0_0_gate(Uml3_0_0_gate uml3_0_0_gate) {
        this.uml3_0_0_gates.add(uml3_0_0_gate);
    }
    public uml3_0_0_Interaction getUml3_0_0_interaction() {
        return uml3_0_0_interaction;
    }

    public void setUml3_0_0_interaction(uml3_0_0_Interaction uml3_0_0_interaction) {
        this.uml3_0_0_interaction = uml3_0_0_interaction;
    }

}