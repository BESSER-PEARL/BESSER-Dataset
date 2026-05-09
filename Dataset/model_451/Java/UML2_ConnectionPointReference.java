





import java.util.List;
import java.util.ArrayList;

public class UML2_ConnectionPointReference extends Vertex {






    private UML2_State uml2_state;




    private List<UML2_Pseudostate> uml2_pseudostates;




    private List<UML2_Pseudostate> uml2_pseudostates;


    public UML2_ConnectionPointReference(
    ) {
        super(
        );
        this.uml2_pseudostates = new ArrayList<>();
        this.uml2_pseudostates = new ArrayList<>();
    }

    public UML2_ConnectionPointReference(
        ArrayList<UML2_Pseudostate> uml2_pseudostates,        ArrayList<UML2_Pseudostate> uml2_pseudostates    ) {
        this.uml2_pseudostates = uml2_pseudostates;
        this.uml2_pseudostates = uml2_pseudostates;
    }


    public UML2_State getUml2_state() {
        return uml2_state;
    }

    public void setUml2_state(UML2_State uml2_state) {
        this.uml2_state = uml2_state;
    }
    public List<UML2_Pseudostate> getUml2_pseudostates() {
        return uml2_pseudostates;
    }

    public void addUml2_pseudostate(Uml2_pseudostate uml2_pseudostate) {
        this.uml2_pseudostates.add(uml2_pseudostate);
    }
    public List<UML2_Pseudostate> getUml2_pseudostates() {
        return uml2_pseudostates;
    }

    public void addUml2_pseudostate(Uml2_pseudostate uml2_pseudostate) {
        this.uml2_pseudostates.add(uml2_pseudostate);
    }

}