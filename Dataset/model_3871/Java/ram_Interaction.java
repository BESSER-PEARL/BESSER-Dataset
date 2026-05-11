





import java.util.List;
import java.util.ArrayList;

public class ram_Interaction extends FragmentContainer {






    private List<ram_Reference> ram_references;




    private List<ram_Gate> ram_gates;




    private ram_AspectMessageView ram_aspectmessageview;


    public ram_Interaction(
    ) {
        super(
        );
        this.ram_references = new ArrayList<>();
        this.ram_gates = new ArrayList<>();
    }

    public ram_Interaction(
        ArrayList<ram_Reference> ram_references,        ArrayList<ram_Gate> ram_gates    ) {
        this.ram_references = ram_references;
        this.ram_gates = ram_gates;
    }


    public List<ram_Reference> getRam_references() {
        return ram_references;
    }

    public void addRam_reference(Ram_reference ram_reference) {
        this.ram_references.add(ram_reference);
    }
    public List<ram_Gate> getRam_gates() {
        return ram_gates;
    }

    public void addRam_gate(Ram_gate ram_gate) {
        this.ram_gates.add(ram_gate);
    }
    public ram_AspectMessageView getRam_aspectmessageview() {
        return ram_aspectmessageview;
    }

    public void setRam_aspectmessageview(ram_AspectMessageView ram_aspectmessageview) {
        this.ram_aspectmessageview = ram_aspectmessageview;
    }

}