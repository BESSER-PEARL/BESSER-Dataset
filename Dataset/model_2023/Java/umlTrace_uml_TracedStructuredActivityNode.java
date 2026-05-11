





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedStructuredActivityNode extends uml_TracedAction, uml_TracedActivityGroup, uml_TracedNamespace {






    private List<uml_TracedActivityNode> uml_tracedactivitynodes;




    private List<uml_TracedVariable> uml_tracedvariables;




    private List<uml_TracedOutputPin> uml_tracedoutputpins;




    private List<uml_TracedInputPin> uml_tracedinputpins;




    private List<uml_TracedActivityEdge> uml_tracedactivityedges;


    public umlTrace_uml_TracedStructuredActivityNode(
    ) {
        super(
        );
        this.uml_tracedactivitynodes = new ArrayList<>();
        this.uml_tracedvariables = new ArrayList<>();
        this.uml_tracedoutputpins = new ArrayList<>();
        this.uml_tracedinputpins = new ArrayList<>();
        this.uml_tracedactivityedges = new ArrayList<>();
    }

    public umlTrace_uml_TracedStructuredActivityNode(
        ArrayList<uml_TracedActivityNode> uml_tracedactivitynodes,        ArrayList<uml_TracedVariable> uml_tracedvariables,        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins,        ArrayList<uml_TracedInputPin> uml_tracedinputpins,        ArrayList<uml_TracedActivityEdge> uml_tracedactivityedges    ) {
        this.uml_tracedactivitynodes = uml_tracedactivitynodes;
        this.uml_tracedvariables = uml_tracedvariables;
        this.uml_tracedoutputpins = uml_tracedoutputpins;
        this.uml_tracedinputpins = uml_tracedinputpins;
        this.uml_tracedactivityedges = uml_tracedactivityedges;
    }


    public List<uml_TracedActivityNode> getUml_tracedactivitynodes() {
        return uml_tracedactivitynodes;
    }

    public void addUml_tracedactivitynode(Uml_tracedactivitynode uml_tracedactivitynode) {
        this.uml_tracedactivitynodes.add(uml_tracedactivitynode);
    }
    public List<uml_TracedVariable> getUml_tracedvariables() {
        return uml_tracedvariables;
    }

    public void addUml_tracedvariable(Uml_tracedvariable uml_tracedvariable) {
        this.uml_tracedvariables.add(uml_tracedvariable);
    }
    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }
    public List<uml_TracedInputPin> getUml_tracedinputpins() {
        return uml_tracedinputpins;
    }

    public void addUml_tracedinputpin(Uml_tracedinputpin uml_tracedinputpin) {
        this.uml_tracedinputpins.add(uml_tracedinputpin);
    }
    public List<uml_TracedActivityEdge> getUml_tracedactivityedges() {
        return uml_tracedactivityedges;
    }

    public void addUml_tracedactivityedge(Uml_tracedactivityedge uml_tracedactivityedge) {
        this.uml_tracedactivityedges.add(uml_tracedactivityedge);
    }

}