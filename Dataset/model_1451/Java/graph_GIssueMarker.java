





import java.util.List;
import java.util.ArrayList;

public class graph_GIssueMarker extends GShapeElement {






    private List<graph_GIssue> graph_gissues;


    public graph_GIssueMarker(
    ) {
        super(
        );
        this.graph_gissues = new ArrayList<>();
    }

    public graph_GIssueMarker(
        ArrayList<graph_GIssue> graph_gissues    ) {
        this.graph_gissues = graph_gissues;
    }


    public List<graph_GIssue> getGraph_gissues() {
        return graph_gissues;
    }

    public void addGraph_gissue(Graph_gissue graph_gissue) {
        this.graph_gissues.add(graph_gissue);
    }

}