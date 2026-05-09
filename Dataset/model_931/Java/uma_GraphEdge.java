





import java.util.List;
import java.util.ArrayList;

public class uma_GraphEdge extends GraphElement {






    private List<uma_GraphConnector> uma_graphconnectors;




    private uma_GraphConnector uma_graphconnector;




    private List<uma_Point> uma_points;


    public uma_GraphEdge(
    ) {
        super(
        );
        this.uma_graphconnectors = new ArrayList<>();
        this.uma_points = new ArrayList<>();
    }

    public uma_GraphEdge(
        ArrayList<uma_GraphConnector> uma_graphconnectors,        ArrayList<uma_Point> uma_points    ) {
        this.uma_graphconnectors = uma_graphconnectors;
        this.uma_points = uma_points;
    }


    public List<uma_GraphConnector> getUma_graphconnectors() {
        return uma_graphconnectors;
    }

    public void addUma_graphconnector(Uma_graphconnector uma_graphconnector) {
        this.uma_graphconnectors.add(uma_graphconnector);
    }
    public uma_GraphConnector getUma_graphconnector() {
        return uma_graphconnector;
    }

    public void setUma_graphconnector(uma_GraphConnector uma_graphconnector) {
        this.uma_graphconnector = uma_graphconnector;
    }
    public List<uma_Point> getUma_points() {
        return uma_points;
    }

    public void addUma_point(Uma_point uma_point) {
        this.uma_points.add(uma_point);
    }

}