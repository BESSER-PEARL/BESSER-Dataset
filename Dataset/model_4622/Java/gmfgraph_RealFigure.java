





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_RealFigure extends AbstractFigure {

    private String name;





    private gmfgraph_FigureGallery gmfgraph_figuregallery;


    public gmfgraph_RealFigure(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gmfgraph_FigureGallery getGmfgraph_figuregallery() {
        return gmfgraph_figuregallery;
    }

    public void setGmfgraph_figuregallery(gmfgraph_FigureGallery gmfgraph_figuregallery) {
        this.gmfgraph_figuregallery = gmfgraph_figuregallery;
    }

}