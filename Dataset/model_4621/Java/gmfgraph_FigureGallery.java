





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureGallery extends Identity {

    private String implementationBundle;





    private gmfgraph_Canvas gmfgraph_canvas;




    private List<gmfgraph_RealFigure> gmfgraph_realfigures;


    public gmfgraph_FigureGallery(
        String implementationBundle    ) {
        super(
        );
        this.implementationBundle = implementationBundle;
        this.gmfgraph_realfigures = new ArrayList<>();
    }

    public gmfgraph_FigureGallery(
        String implementationBundle        ArrayList<gmfgraph_RealFigure> gmfgraph_realfigures    ) {
        this.implementationBundle = implementationBundle;
        this.gmfgraph_realfigures = gmfgraph_realfigures;
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
    public List<gmfgraph_RealFigure> getGmfgraph_realfigures() {
        return gmfgraph_realfigures;
    }

    public void addGmfgraph_realfigure(Gmfgraph_realfigure gmfgraph_realfigure) {
        this.gmfgraph_realfigures.add(gmfgraph_realfigure);
    }

}