





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureGallery extends Identity {

    private String implementationBundle;





    private List<gmfgraph_FigureDescriptor> gmfgraph_figuredescriptors;




    private gmfgraph_Canvas gmfgraph_canvas;


    public gmfgraph_FigureGallery(
        String implementationBundle    ) {
        super(
        );
        this.implementationBundle = implementationBundle;
        this.gmfgraph_figuredescriptors = new ArrayList<>();
    }

    public gmfgraph_FigureGallery(
        String implementationBundle        ArrayList<gmfgraph_FigureDescriptor> gmfgraph_figuredescriptors    ) {
        this.implementationBundle = implementationBundle;
        this.gmfgraph_figuredescriptors = gmfgraph_figuredescriptors;
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
    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }

}