





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureGallery extends Identity {

    private String implementationBundle;





    private gmfgraph_Canvas gmfgraph_canvas;




    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_FigureGallery(
        String implementationBundle    ) {
        super(
        );
        this.implementationBundle = implementationBundle;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_FigureGallery(
        String implementationBundle        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.implementationBundle = implementationBundle;
        this.gmfgraph_figures = gmfgraph_figures;
    }

    public String getImplementationbundle() {
        return implementationBundle;
    }

    public void setImplementationbundle(String implementationBundle) {
        this.implementationBundle = implementationBundle;
    }

    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }
    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }

}