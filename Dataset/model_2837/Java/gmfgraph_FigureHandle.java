





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureHandle  {






    private List<gmfgraph_DiagramElement> gmfgraph_diagramelements;




    private gmfgraph_DiagramElement gmfgraph_diagramelement;


    public gmfgraph_FigureHandle(
    ) {
        this.gmfgraph_diagramelements = new ArrayList<>();
    }

    public gmfgraph_FigureHandle(
        ArrayList<gmfgraph_DiagramElement> gmfgraph_diagramelements    ) {
        this.gmfgraph_diagramelements = gmfgraph_diagramelements;
    }


    public List<gmfgraph_DiagramElement> getGmfgraph_diagramelements() {
        return gmfgraph_diagramelements;
    }

    public void addGmfgraph_diagramelement(Gmfgraph_diagramelement gmfgraph_diagramelement) {
        this.gmfgraph_diagramelements.add(gmfgraph_diagramelement);
    }
    public gmfgraph_DiagramElement getGmfgraph_diagramelement() {
        return gmfgraph_diagramelement;
    }

    public void setGmfgraph_diagramelement(gmfgraph_DiagramElement gmfgraph_diagramelement) {
        this.gmfgraph_diagramelement = gmfgraph_diagramelement;
    }

}