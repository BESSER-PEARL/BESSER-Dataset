





import java.util.List;
import java.util.ArrayList;

public class uml_ConnectionPointReference extends Vertex {






    private List<uml_Pseudostate> uml_pseudostates;




    private List<uml_Pseudostate> uml_pseudostates;




    private uml_State uml_state;




    private uml_State uml_state;


    public uml_ConnectionPointReference(
    ) {
        super(
        );
        this.uml_pseudostates = new ArrayList<>();
        this.uml_pseudostates = new ArrayList<>();
    }

    public uml_ConnectionPointReference(
        ArrayList<uml_Pseudostate> uml_pseudostates,        ArrayList<uml_Pseudostate> uml_pseudostates    ) {
        this.uml_pseudostates = uml_pseudostates;
        this.uml_pseudostates = uml_pseudostates;
    }


    public List<uml_Pseudostate> getUml_pseudostates() {
        return uml_pseudostates;
    }

    public void addUml_pseudostate(Uml_pseudostate uml_pseudostate) {
        this.uml_pseudostates.add(uml_pseudostate);
    }
    public List<uml_Pseudostate> getUml_pseudostates() {
        return uml_pseudostates;
    }

    public void addUml_pseudostate(Uml_pseudostate uml_pseudostate) {
        this.uml_pseudostates.add(uml_pseudostate);
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }
    public uml_State getUml_state() {
        return uml_state;
    }

    public void setUml_state(uml_State uml_state) {
        this.uml_state = uml_state;
    }

}