





import java.util.List;
import java.util.ArrayList;

public class uma_GraphElement extends DiagramElement {






    private List<uma_DiagramElement> uma_diagramelements;




    private uma_Point uma_point;




    private uma_DiagramElement uma_diagramelement;


    public uma_GraphElement(
    ) {
        super(
        );
        this.uma_diagramelements = new ArrayList<>();
    }

    public uma_GraphElement(
        ArrayList<uma_DiagramElement> uma_diagramelements    ) {
        this.uma_diagramelements = uma_diagramelements;
    }


    public List<uma_DiagramElement> getUma_diagramelements() {
        return uma_diagramelements;
    }

    public void addUma_diagramelement(Uma_diagramelement uma_diagramelement) {
        this.uma_diagramelements.add(uma_diagramelement);
    }
    public uma_Point getUma_point() {
        return uma_point;
    }

    public void setUma_point(uma_Point uma_point) {
        this.uma_point = uma_point;
    }
    public uma_DiagramElement getUma_diagramelement() {
        return uma_diagramelement;
    }

    public void setUma_diagramelement(uma_DiagramElement uma_diagramelement) {
        this.uma_diagramelement = uma_diagramelement;
    }

}