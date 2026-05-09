





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ConnectionPointReference extends Vertex {






    private List<UML2WithID_Pseudostate> uml2withid_pseudostates;




    private UML2WithID_State uml2withid_state;




    private List<UML2WithID_Pseudostate> uml2withid_pseudostates;


    public UML2WithID_ConnectionPointReference(
    ) {
        super(
        );
        this.uml2withid_pseudostates = new ArrayList<>();
        this.uml2withid_pseudostates = new ArrayList<>();
    }

    public UML2WithID_ConnectionPointReference(
        ArrayList<UML2WithID_Pseudostate> uml2withid_pseudostates,        ArrayList<UML2WithID_Pseudostate> uml2withid_pseudostates    ) {
        this.uml2withid_pseudostates = uml2withid_pseudostates;
        this.uml2withid_pseudostates = uml2withid_pseudostates;
    }


    public List<UML2WithID_Pseudostate> getUml2withid_pseudostates() {
        return uml2withid_pseudostates;
    }

    public void addUml2withid_pseudostate(Uml2withid_pseudostate uml2withid_pseudostate) {
        this.uml2withid_pseudostates.add(uml2withid_pseudostate);
    }
    public UML2WithID_State getUml2withid_state() {
        return uml2withid_state;
    }

    public void setUml2withid_state(UML2WithID_State uml2withid_state) {
        this.uml2withid_state = uml2withid_state;
    }
    public List<UML2WithID_Pseudostate> getUml2withid_pseudostates() {
        return uml2withid_pseudostates;
    }

    public void addUml2withid_pseudostate(Uml2withid_pseudostate uml2withid_pseudostate) {
        this.uml2withid_pseudostates.add(uml2withid_pseudostate);
    }

}