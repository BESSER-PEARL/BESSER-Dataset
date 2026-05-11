





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_DiagramElement extends Identity {






    private List<gmfgraph_VisualFacet> gmfgraph_visualfacets;




    private gmfgraph_FigureHandle gmfgraph_figurehandle;




    private gmfgraph_FigureHandle gmfgraph_figurehandle;


    public gmfgraph_DiagramElement(
    ) {
        super(
        );
        this.gmfgraph_visualfacets = new ArrayList<>();
    }

    public gmfgraph_DiagramElement(
        ArrayList<gmfgraph_VisualFacet> gmfgraph_visualfacets    ) {
        this.gmfgraph_visualfacets = gmfgraph_visualfacets;
    }


    public List<gmfgraph_VisualFacet> getGmfgraph_visualfacets() {
        return gmfgraph_visualfacets;
    }

    public void addGmfgraph_visualfacet(Gmfgraph_visualfacet gmfgraph_visualfacet) {
        this.gmfgraph_visualfacets.add(gmfgraph_visualfacet);
    }
    public gmfgraph_FigureHandle getGmfgraph_figurehandle() {
        return gmfgraph_figurehandle;
    }

    public void setGmfgraph_figurehandle(gmfgraph_FigureHandle gmfgraph_figurehandle) {
        this.gmfgraph_figurehandle = gmfgraph_figurehandle;
    }
    public gmfgraph_FigureHandle getGmfgraph_figurehandle() {
        return gmfgraph_figurehandle;
    }

    public void setGmfgraph_figurehandle(gmfgraph_FigureHandle gmfgraph_figurehandle) {
        this.gmfgraph_figurehandle = gmfgraph_figurehandle;
    }

}