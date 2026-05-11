





import java.util.List;
import java.util.ArrayList;

public class faultTree_Event  {

    private String description;
    private String name;





    private List<faultTree_Gate> faulttree_gates;




    private faultTree_FaultTree faulttree_faulttree;




    private faultTree_FaultTree faulttree_faulttree;




    private faultTree_Gate faulttree_gate;


    public faultTree_Event(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.faulttree_gates = new ArrayList<>();
    }

    public faultTree_Event(
        String description,        String name        ArrayList<faultTree_Gate> faulttree_gates    ) {
        this.description = description;
        this.name = name;
        this.faulttree_gates = faulttree_gates;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<faultTree_Gate> getFaulttree_gates() {
        return faulttree_gates;
    }

    public void addFaulttree_gate(Faulttree_gate faulttree_gate) {
        this.faulttree_gates.add(faulttree_gate);
    }
    public faultTree_FaultTree getFaulttree_faulttree() {
        return faulttree_faulttree;
    }

    public void setFaulttree_faulttree(faultTree_FaultTree faulttree_faulttree) {
        this.faulttree_faulttree = faulttree_faulttree;
    }
    public faultTree_FaultTree getFaulttree_faulttree() {
        return faulttree_faulttree;
    }

    public void setFaulttree_faulttree(faultTree_FaultTree faulttree_faulttree) {
        this.faulttree_faulttree = faulttree_faulttree;
    }
    public faultTree_Gate getFaulttree_gate() {
        return faulttree_gate;
    }

    public void setFaulttree_gate(faultTree_Gate faulttree_gate) {
        this.faulttree_gate = faulttree_gate;
    }

}