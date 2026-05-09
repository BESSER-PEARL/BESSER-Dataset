





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ConnectionPointReference extends Vertex {






    private uml3_0_0_State uml3_0_0_state;




    private uml3_0_0_State uml3_0_0_state;




    private List<uml3_0_0_Pseudostate> uml3_0_0_pseudostates;




    private List<uml3_0_0_Pseudostate> uml3_0_0_pseudostates;


    public uml3_0_0_ConnectionPointReference(
    ) {
        super(
        );
        this.uml3_0_0_pseudostates = new ArrayList<>();
        this.uml3_0_0_pseudostates = new ArrayList<>();
    }

    public uml3_0_0_ConnectionPointReference(
        ArrayList<uml3_0_0_Pseudostate> uml3_0_0_pseudostates,        ArrayList<uml3_0_0_Pseudostate> uml3_0_0_pseudostates    ) {
        this.uml3_0_0_pseudostates = uml3_0_0_pseudostates;
        this.uml3_0_0_pseudostates = uml3_0_0_pseudostates;
    }


    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public uml3_0_0_State getUml3_0_0_state() {
        return uml3_0_0_state;
    }

    public void setUml3_0_0_state(uml3_0_0_State uml3_0_0_state) {
        this.uml3_0_0_state = uml3_0_0_state;
    }
    public List<uml3_0_0_Pseudostate> getUml3_0_0_pseudostates() {
        return uml3_0_0_pseudostates;
    }

    public void addUml3_0_0_pseudostate(Uml3_0_0_pseudostate uml3_0_0_pseudostate) {
        this.uml3_0_0_pseudostates.add(uml3_0_0_pseudostate);
    }
    public List<uml3_0_0_Pseudostate> getUml3_0_0_pseudostates() {
        return uml3_0_0_pseudostates;
    }

    public void addUml3_0_0_pseudostate(Uml3_0_0_pseudostate uml3_0_0_pseudostate) {
        this.uml3_0_0_pseudostates.add(uml3_0_0_pseudostate);
    }

}