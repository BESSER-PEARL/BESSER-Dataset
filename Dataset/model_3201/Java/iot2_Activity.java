





import java.util.List;
import java.util.ArrayList;

public class iot2_Activity extends NamedElement {






    private List<iot2_ActivityNode> iot2_activitynodes;




    private List<iot2_Variable> iot2_variables;




    private List<iot2_ActivityEdge> iot2_activityedges;




    private List<iot2_Variable> iot2_variables;




    private iot2_Sketch iot2_sketch;




    private iot2_ActivityNode iot2_activitynode;




    private iot2_Context iot2_context;


    public iot2_Activity(
    ) {
        super(
        );
        this.iot2_activitynodes = new ArrayList<>();
        this.iot2_variables = new ArrayList<>();
        this.iot2_activityedges = new ArrayList<>();
        this.iot2_variables = new ArrayList<>();
    }

    public iot2_Activity(
        ArrayList<iot2_ActivityNode> iot2_activitynodes,        ArrayList<iot2_Variable> iot2_variables,        ArrayList<iot2_ActivityEdge> iot2_activityedges,        ArrayList<iot2_Variable> iot2_variables    ) {
        this.iot2_activitynodes = iot2_activitynodes;
        this.iot2_variables = iot2_variables;
        this.iot2_activityedges = iot2_activityedges;
        this.iot2_variables = iot2_variables;
    }


    public List<iot2_ActivityNode> getIot2_activitynodes() {
        return iot2_activitynodes;
    }

    public void addIot2_activitynode(Iot2_activitynode iot2_activitynode) {
        this.iot2_activitynodes.add(iot2_activitynode);
    }
    public List<iot2_Variable> getIot2_variables() {
        return iot2_variables;
    }

    public void addIot2_variable(Iot2_variable iot2_variable) {
        this.iot2_variables.add(iot2_variable);
    }
    public List<iot2_ActivityEdge> getIot2_activityedges() {
        return iot2_activityedges;
    }

    public void addIot2_activityedge(Iot2_activityedge iot2_activityedge) {
        this.iot2_activityedges.add(iot2_activityedge);
    }
    public List<iot2_Variable> getIot2_variables() {
        return iot2_variables;
    }

    public void addIot2_variable(Iot2_variable iot2_variable) {
        this.iot2_variables.add(iot2_variable);
    }
    public iot2_Sketch getIot2_sketch() {
        return iot2_sketch;
    }

    public void setIot2_sketch(iot2_Sketch iot2_sketch) {
        this.iot2_sketch = iot2_sketch;
    }
    public iot2_ActivityNode getIot2_activitynode() {
        return iot2_activitynode;
    }

    public void setIot2_activitynode(iot2_ActivityNode iot2_activitynode) {
        this.iot2_activitynode = iot2_activitynode;
    }
    public iot2_Context getIot2_context() {
        return iot2_context;
    }

    public void setIot2_context(iot2_Context iot2_context) {
        this.iot2_context = iot2_context;
    }

}