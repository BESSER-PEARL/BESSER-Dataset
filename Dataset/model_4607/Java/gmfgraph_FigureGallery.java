





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureGallery extends Identity {

    private String implementationBundle;





    private List<gmfgraph_FigureDescriptor> gmfgraph_figuredescriptors;




    private List<gmfgraph_Border> gmfgraph_borders;




    private List<gmfgraph_RealFigure> gmfgraph_realfigures;




    private List<gmfgraph_Layout> gmfgraph_layouts;




    private gmfgraph_Canvas gmfgraph_canvas;


    public gmfgraph_FigureGallery(
        String implementationBundle    ) {
        super(
        );
        this.implementationBundle = implementationBundle;
        this.gmfgraph_figuredescriptors = new ArrayList<>();
        this.gmfgraph_borders = new ArrayList<>();
        this.gmfgraph_realfigures = new ArrayList<>();
        this.gmfgraph_layouts = new ArrayList<>();
    }

    public gmfgraph_FigureGallery(
        String implementationBundle        ArrayList<gmfgraph_FigureDescriptor> gmfgraph_figuredescriptors,        ArrayList<gmfgraph_Border> gmfgraph_borders,        ArrayList<gmfgraph_RealFigure> gmfgraph_realfigures,        ArrayList<gmfgraph_Layout> gmfgraph_layouts    ) {
        this.implementationBundle = implementationBundle;
        this.gmfgraph_figuredescriptors = gmfgraph_figuredescriptors;
        this.gmfgraph_borders = gmfgraph_borders;
        this.gmfgraph_realfigures = gmfgraph_realfigures;
        this.gmfgraph_layouts = gmfgraph_layouts;
    }

    public String getImplementationbundle() {
        return implementationBundle;
    }

    public void setImplementationbundle(String implementationBundle) {
        this.implementationBundle = implementationBundle;
    }

    public List<gmfgraph_FigureDescriptor> getGmfgraph_figuredescriptors() {
        return gmfgraph_figuredescriptors;
    }

    public void addGmfgraph_figuredescriptor(Gmfgraph_figuredescriptor gmfgraph_figuredescriptor) {
        this.gmfgraph_figuredescriptors.add(gmfgraph_figuredescriptor);
    }
    public List<gmfgraph_Border> getGmfgraph_borders() {
        return gmfgraph_borders;
    }

    public void addGmfgraph_border(Gmfgraph_border gmfgraph_border) {
        this.gmfgraph_borders.add(gmfgraph_border);
    }
    public List<gmfgraph_RealFigure> getGmfgraph_realfigures() {
        return gmfgraph_realfigures;
    }

    public void addGmfgraph_realfigure(Gmfgraph_realfigure gmfgraph_realfigure) {
        this.gmfgraph_realfigures.add(gmfgraph_realfigure);
    }
    public List<gmfgraph_Layout> getGmfgraph_layouts() {
        return gmfgraph_layouts;
    }

    public void addGmfgraph_layout(Gmfgraph_layout gmfgraph_layout) {
        this.gmfgraph_layouts.add(gmfgraph_layout);
    }
    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }

}