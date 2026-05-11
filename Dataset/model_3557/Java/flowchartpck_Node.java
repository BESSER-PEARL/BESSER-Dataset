





import java.util.List;
import java.util.ArrayList;

public class flowchartpck_Node extends NamedElement {






    private flowchartpck_Flowchart flowchartpck_flowchart;




    private flowchartpck_Arc flowchartpck_arc;




    private List<flowchartpck_Arc> flowchartpck_arcs;




    private flowchartpck_Arc flowchartpck_arc;




    private List<flowchartpck_Arc> flowchartpck_arcs;


    public flowchartpck_Node(
    ) {
        super(
        );
        this.flowchartpck_arcs = new ArrayList<>();
        this.flowchartpck_arcs = new ArrayList<>();
    }

    public flowchartpck_Node(
        ArrayList<flowchartpck_Arc> flowchartpck_arcs,        ArrayList<flowchartpck_Arc> flowchartpck_arcs    ) {
        this.flowchartpck_arcs = flowchartpck_arcs;
        this.flowchartpck_arcs = flowchartpck_arcs;
    }


    public flowchartpck_Flowchart getFlowchartpck_flowchart() {
        return flowchartpck_flowchart;
    }

    public void setFlowchartpck_flowchart(flowchartpck_Flowchart flowchartpck_flowchart) {
        this.flowchartpck_flowchart = flowchartpck_flowchart;
    }
    public flowchartpck_Arc getFlowchartpck_arc() {
        return flowchartpck_arc;
    }

    public void setFlowchartpck_arc(flowchartpck_Arc flowchartpck_arc) {
        this.flowchartpck_arc = flowchartpck_arc;
    }
    public List<flowchartpck_Arc> getFlowchartpck_arcs() {
        return flowchartpck_arcs;
    }

    public void addFlowchartpck_arc(Flowchartpck_arc flowchartpck_arc) {
        this.flowchartpck_arcs.add(flowchartpck_arc);
    }
    public flowchartpck_Arc getFlowchartpck_arc() {
        return flowchartpck_arc;
    }

    public void setFlowchartpck_arc(flowchartpck_Arc flowchartpck_arc) {
        this.flowchartpck_arc = flowchartpck_arc;
    }
    public List<flowchartpck_Arc> getFlowchartpck_arcs() {
        return flowchartpck_arcs;
    }

    public void addFlowchartpck_arc(Flowchartpck_arc flowchartpck_arc) {
        this.flowchartpck_arcs.add(flowchartpck_arc);
    }

}