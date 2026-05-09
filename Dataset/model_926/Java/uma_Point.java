





import java.util.List;
import java.util.ArrayList;

public class uma_Point  {

    private String y;
    private String x;





    private uma_DiagramLink uma_diagramlink;




    private uma_GraphElement uma_graphelement;




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

    public uma_DiagramLink getUma_diagramlink() {
        return uma_diagramlink;
    }

    public void setUma_diagramlink(uma_DiagramLink uma_diagramlink) {
        this.uma_diagramlink = uma_diagramlink;
    }
    public uma_GraphElement getUma_graphelement() {
        return uma_graphelement;
    }

    public void setUma_graphelement(uma_GraphElement uma_graphelement) {
        this.uma_graphelement = uma_graphelement;
    }
    public uma_Diagram getUma_diagram() {
        return uma_diagram;
    }

    public void setUma_diagram(uma_Diagram uma_diagram) {
        this.uma_diagram = uma_diagram;
    }

}