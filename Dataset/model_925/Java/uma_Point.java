





import java.util.List;
import java.util.ArrayList;

public class uma_Point  {

    private String x;
    private String y;





    private uma_Diagram uma_diagram;




    private uma_DiagramLink uma_diagramlink;


    public uma_Point(
        String x,        String y    ) {
        this.x = x;
        this.y = y;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public uma_Diagram getUma_diagram() {
        return uma_diagram;
    }

    public void setUma_diagram(uma_Diagram uma_diagram) {
        this.uma_diagram = uma_diagram;
    }
    public uma_DiagramLink getUma_diagramlink() {
        return uma_diagramlink;
    }

    public void setUma_diagramlink(uma_DiagramLink uma_diagramlink) {
        this.uma_diagramlink = uma_diagramlink;
    }

}