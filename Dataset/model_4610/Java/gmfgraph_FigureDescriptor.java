





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureDescriptor extends Identity {






    private gmfgraph_ChildAccess gmfgraph_childaccess;




    private gmfgraph_DiagramElement gmfgraph_diagramelement;




    private gmfgraph_Figure gmfgraph_figure;




    private List<gmfgraph_ChildAccess> gmfgraph_childaccesss;




    private gmfgraph_Figure gmfgraph_figure;


    public gmfgraph_FigureDescriptor(
    ) {
        super(
        );
        this.gmfgraph_childaccesss = new ArrayList<>();
    }

    public gmfgraph_FigureDescriptor(
        ArrayList<gmfgraph_ChildAccess> gmfgraph_childaccesss    ) {
        this.gmfgraph_childaccesss = gmfgraph_childaccesss;
    }


    public gmfgraph_ChildAccess getGmfgraph_childaccess() {
        return gmfgraph_childaccess;
    }

    public void setGmfgraph_childaccess(gmfgraph_ChildAccess gmfgraph_childaccess) {
        this.gmfgraph_childaccess = gmfgraph_childaccess;
    }
    public gmfgraph_DiagramElement getGmfgraph_diagramelement() {
        return gmfgraph_diagramelement;
    }

    public void setGmfgraph_diagramelement(gmfgraph_DiagramElement gmfgraph_diagramelement) {
        this.gmfgraph_diagramelement = gmfgraph_diagramelement;
    }
    public gmfgraph_Figure getGmfgraph_figure() {
        return gmfgraph_figure;
    }

    public void setGmfgraph_figure(gmfgraph_Figure gmfgraph_figure) {
        this.gmfgraph_figure = gmfgraph_figure;
    }
    public List<gmfgraph_ChildAccess> getGmfgraph_childaccesss() {
        return gmfgraph_childaccesss;
    }

    public void addGmfgraph_childaccess(Gmfgraph_childaccess gmfgraph_childaccess) {
        this.gmfgraph_childaccesss.add(gmfgraph_childaccess);
    }
    public gmfgraph_Figure getGmfgraph_figure() {
        return gmfgraph_figure;
    }

    public void setGmfgraph_figure(gmfgraph_Figure gmfgraph_figure) {
        this.gmfgraph_figure = gmfgraph_figure;
    }

}