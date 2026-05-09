





import java.util.List;
import java.util.ArrayList;

public class graph_Edge extends Identifiable {

    private boolean visited;
    private int EdgeLabel;



    public graph_Edge(
        boolean visited,        int EdgeLabel    ) {
        super(
        );
        this.visited = visited;
        this.EdgeLabel = EdgeLabel;
    }


    public boolean getVisited() {
        return visited;
    }

    public void setVisited(boolean visited) {
        this.visited = visited;
    }
    public int getEdgelabel() {
        return EdgeLabel;
    }

    public void setEdgelabel(int EdgeLabel) {
        this.EdgeLabel = EdgeLabel;
    }


}