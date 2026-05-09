





import java.util.List;
import java.util.ArrayList;

public class graph_ElkEdgeSection extends EMapPropertyHolder {

    private float endY;
    private float startY;
    private float endX;
    private String identifier;
    private float startX;





    private graph_ElkEdgeSection graph_elkedgesection;




    private List<graph_ElkEdgeSection> graph_elkedgesections;


    public graph_ElkEdgeSection(
        float endY,        float startY,        float endX,        String identifier,        float startX    ) {
        super(
        );
        this.endY = endY;
        this.startY = startY;
        this.endX = endX;
        this.identifier = identifier;
        this.startX = startX;
        this.graph_elkedgesections = new ArrayList<>();
    }

    public graph_ElkEdgeSection(
        float endY,        float startY,        float endX,        String identifier,        float startX        ArrayList<graph_ElkEdgeSection> graph_elkedgesections    ) {
        this.endY = endY;
        this.startY = startY;
        this.endX = endX;
        this.identifier = identifier;
        this.startX = startX;
        this.graph_elkedgesections = graph_elkedgesections;
    }

    public float getEndy() {
        return endY;
    }

    public void setEndy(float endY) {
        this.endY = endY;
    }
    public float getStarty() {
        return startY;
    }

    public void setStarty(float startY) {
        this.startY = startY;
    }
    public float getEndx() {
        return endX;
    }

    public void setEndx(float endX) {
        this.endX = endX;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public float getStartx() {
        return startX;
    }

    public void setStartx(float startX) {
        this.startX = startX;
    }

    public graph_ElkEdgeSection getGraph_elkedgesection() {
        return graph_elkedgesection;
    }

    public void setGraph_elkedgesection(graph_ElkEdgeSection graph_elkedgesection) {
        this.graph_elkedgesection = graph_elkedgesection;
    }
    public List<graph_ElkEdgeSection> getGraph_elkedgesections() {
        return graph_elkedgesections;
    }

    public void addGraph_elkedgesection(Graph_elkedgesection graph_elkedgesection) {
        this.graph_elkedgesections.add(graph_elkedgesection);
    }

}