





import java.util.List;
import java.util.ArrayList;

public class qVTcDataDependencyGraph_Node extends Element {

    private String label;





    private List<qVTcDataDependencyGraph_Edge> qvtcdatadependencygraph_edges;




    private List<qVTcDataDependencyGraph_Edge> qvtcdatadependencygraph_edges;




    private qVTcDataDependencyGraph_Edge qvtcdatadependencygraph_edge;




    private qVTcDataDependencyGraph_EObject qvtcdatadependencygraph_eobject;




    private qVTcDataDependencyGraph_Edge qvtcdatadependencygraph_edge;


    public qVTcDataDependencyGraph_Node(
        String label    ) {
        super(
        );
        this.label = label;
        this.qvtcdatadependencygraph_edges = new ArrayList<>();
        this.qvtcdatadependencygraph_edges = new ArrayList<>();
    }

    public qVTcDataDependencyGraph_Node(
        String label        ArrayList<qVTcDataDependencyGraph_Edge> qvtcdatadependencygraph_edges,        ArrayList<qVTcDataDependencyGraph_Edge> qvtcdatadependencygraph_edges    ) {
        this.label = label;
        this.qvtcdatadependencygraph_edges = qvtcdatadependencygraph_edges;
        this.qvtcdatadependencygraph_edges = qvtcdatadependencygraph_edges;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<qVTcDataDependencyGraph_Edge> getQvtcdatadependencygraph_edges() {
        return qvtcdatadependencygraph_edges;
    }

    public void addQvtcdatadependencygraph_edge(Qvtcdatadependencygraph_edge qvtcdatadependencygraph_edge) {
        this.qvtcdatadependencygraph_edges.add(qvtcdatadependencygraph_edge);
    }
    public List<qVTcDataDependencyGraph_Edge> getQvtcdatadependencygraph_edges() {
        return qvtcdatadependencygraph_edges;
    }

    public void addQvtcdatadependencygraph_edge(Qvtcdatadependencygraph_edge qvtcdatadependencygraph_edge) {
        this.qvtcdatadependencygraph_edges.add(qvtcdatadependencygraph_edge);
    }
    public qVTcDataDependencyGraph_Edge getQvtcdatadependencygraph_edge() {
        return qvtcdatadependencygraph_edge;
    }

    public void setQvtcdatadependencygraph_edge(qVTcDataDependencyGraph_Edge qvtcdatadependencygraph_edge) {
        this.qvtcdatadependencygraph_edge = qvtcdatadependencygraph_edge;
    }
    public qVTcDataDependencyGraph_EObject getQvtcdatadependencygraph_eobject() {
        return qvtcdatadependencygraph_eobject;
    }

    public void setQvtcdatadependencygraph_eobject(qVTcDataDependencyGraph_EObject qvtcdatadependencygraph_eobject) {
        this.qvtcdatadependencygraph_eobject = qvtcdatadependencygraph_eobject;
    }
    public qVTcDataDependencyGraph_Edge getQvtcdatadependencygraph_edge() {
        return qvtcdatadependencygraph_edge;
    }

    public void setQvtcdatadependencygraph_edge(qVTcDataDependencyGraph_Edge qvtcdatadependencygraph_edge) {
        this.qvtcdatadependencygraph_edge = qvtcdatadependencygraph_edge;
    }

}