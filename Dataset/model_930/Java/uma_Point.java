





import java.util.List;
import java.util.ArrayList;

public class uma_Point  {

    private String y;
    private String x;





    private uma_GraphEdge uma_graphedge;




    private uma_Ellipse uma_ellipse;




    private uma_Polyline uma_polyline;




    private uma_Diagram uma_diagram;


    public uma_Point(
        String y,        String x    ) {
        this.y = y;
        this.x = x;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public uma_GraphEdge getUma_graphedge() {
        return uma_graphedge;
    }

    public void setUma_graphedge(uma_GraphEdge uma_graphedge) {
        this.uma_graphedge = uma_graphedge;
    }
    public uma_Ellipse getUma_ellipse() {
        return uma_ellipse;
    }

    public void setUma_ellipse(uma_Ellipse uma_ellipse) {
        this.uma_ellipse = uma_ellipse;
    }
    public uma_Polyline getUma_polyline() {
        return uma_polyline;
    }

    public void setUma_polyline(uma_Polyline uma_polyline) {
        this.uma_polyline = uma_polyline;
    }
    public uma_Diagram getUma_diagram() {
        return uma_diagram;
    }

    public void setUma_diagram(uma_Diagram uma_diagram) {
        this.uma_diagram = uma_diagram;
    }

}