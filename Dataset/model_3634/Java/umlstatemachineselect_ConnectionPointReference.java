





import java.util.List;
import java.util.ArrayList;

public class umlstatemachineselect_ConnectionPointReference extends Vertex {






    private umlstatemachineselect_State umlstatemachineselect_state;




    private List<umlstatemachineselect_PseudoState> umlstatemachineselect_pseudostates;




    private umlstatemachineselect_State umlstatemachineselect_state;




    private List<umlstatemachineselect_PseudoState> umlstatemachineselect_pseudostates;


    public umlstatemachineselect_ConnectionPointReference(
    ) {
        super(
        );
        this.umlstatemachineselect_pseudostates = new ArrayList<>();
        this.umlstatemachineselect_pseudostates = new ArrayList<>();
    }

    public umlstatemachineselect_ConnectionPointReference(
        ArrayList<umlstatemachineselect_PseudoState> umlstatemachineselect_pseudostates,        ArrayList<umlstatemachineselect_PseudoState> umlstatemachineselect_pseudostates    ) {
        this.umlstatemachineselect_pseudostates = umlstatemachineselect_pseudostates;
        this.umlstatemachineselect_pseudostates = umlstatemachineselect_pseudostates;
    }


    public umlstatemachineselect_State getUmlstatemachineselect_state() {
        return umlstatemachineselect_state;
    }

    public void setUmlstatemachineselect_state(umlstatemachineselect_State umlstatemachineselect_state) {
        this.umlstatemachineselect_state = umlstatemachineselect_state;
    }
    public List<umlstatemachineselect_PseudoState> getUmlstatemachineselect_pseudostates() {
        return umlstatemachineselect_pseudostates;
    }

    public void addUmlstatemachineselect_pseudostate(Umlstatemachineselect_pseudostate umlstatemachineselect_pseudostate) {
        this.umlstatemachineselect_pseudostates.add(umlstatemachineselect_pseudostate);
    }
    public umlstatemachineselect_State getUmlstatemachineselect_state() {
        return umlstatemachineselect_state;
    }

    public void setUmlstatemachineselect_state(umlstatemachineselect_State umlstatemachineselect_state) {
        this.umlstatemachineselect_state = umlstatemachineselect_state;
    }
    public List<umlstatemachineselect_PseudoState> getUmlstatemachineselect_pseudostates() {
        return umlstatemachineselect_pseudostates;
    }

    public void addUmlstatemachineselect_pseudostate(Umlstatemachineselect_pseudostate umlstatemachineselect_pseudostate) {
        this.umlstatemachineselect_pseudostates.add(umlstatemachineselect_pseudostate);
    }

}