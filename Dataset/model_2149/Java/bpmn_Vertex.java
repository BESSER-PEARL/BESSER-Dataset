





import java.util.List;
import java.util.ArrayList;

public class bpmn_Vertex extends AssociationTarget {






    private bpmn_SequenceEdge bpmn_sequenceedge;




    private bpmn_Graph bpmn_graph;




    private List<bpmn_SequenceEdge> bpmn_sequenceedges;




    private List<bpmn_SequenceEdge> bpmn_sequenceedges;




    private bpmn_Graph bpmn_graph;




    private bpmn_SequenceEdge bpmn_sequenceedge;


    public bpmn_Vertex(
    ) {
        super(
        );
        this.bpmn_sequenceedges = new ArrayList<>();
        this.bpmn_sequenceedges = new ArrayList<>();
    }

    public bpmn_Vertex(
        ArrayList<bpmn_SequenceEdge> bpmn_sequenceedges,        ArrayList<bpmn_SequenceEdge> bpmn_sequenceedges    ) {
        this.bpmn_sequenceedges = bpmn_sequenceedges;
        this.bpmn_sequenceedges = bpmn_sequenceedges;
    }


    public bpmn_SequenceEdge getBpmn_sequenceedge() {
        return bpmn_sequenceedge;
    }

    public void setBpmn_sequenceedge(bpmn_SequenceEdge bpmn_sequenceedge) {
        this.bpmn_sequenceedge = bpmn_sequenceedge;
    }
    public bpmn_Graph getBpmn_graph() {
        return bpmn_graph;
    }

    public void setBpmn_graph(bpmn_Graph bpmn_graph) {
        this.bpmn_graph = bpmn_graph;
    }
    public List<bpmn_SequenceEdge> getBpmn_sequenceedges() {
        return bpmn_sequenceedges;
    }

    public void addBpmn_sequenceedge(Bpmn_sequenceedge bpmn_sequenceedge) {
        this.bpmn_sequenceedges.add(bpmn_sequenceedge);
    }
    public List<bpmn_SequenceEdge> getBpmn_sequenceedges() {
        return bpmn_sequenceedges;
    }

    public void addBpmn_sequenceedge(Bpmn_sequenceedge bpmn_sequenceedge) {
        this.bpmn_sequenceedges.add(bpmn_sequenceedge);
    }
    public bpmn_Graph getBpmn_graph() {
        return bpmn_graph;
    }

    public void setBpmn_graph(bpmn_Graph bpmn_graph) {
        this.bpmn_graph = bpmn_graph;
    }
    public bpmn_SequenceEdge getBpmn_sequenceedge() {
        return bpmn_sequenceedge;
    }

    public void setBpmn_sequenceedge(bpmn_SequenceEdge bpmn_sequenceedge) {
        this.bpmn_sequenceedge = bpmn_sequenceedge;
    }

}