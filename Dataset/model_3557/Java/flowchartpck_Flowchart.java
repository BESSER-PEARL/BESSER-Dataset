





import java.util.List;
import java.util.ArrayList;

public class flowchartpck_Flowchart extends NamedElement {






    private List<flowchartpck_Arc> flowchartpck_arcs;


    public flowchartpck_Flowchart(
    ) {
        super(
        );
        this.flowchartpck_arcs = new ArrayList<>();
    }

    public flowchartpck_Flowchart(
        ArrayList<flowchartpck_Arc> flowchartpck_arcs    ) {
        this.flowchartpck_arcs = flowchartpck_arcs;
    }


    public List<flowchartpck_Arc> getFlowchartpck_arcs() {
        return flowchartpck_arcs;
    }

    public void addFlowchartpck_arc(Flowchartpck_arc flowchartpck_arc) {
        this.flowchartpck_arcs.add(flowchartpck_arc);
    }

}