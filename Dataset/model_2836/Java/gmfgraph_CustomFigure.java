





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomFigure extends Figure, CustomClass {






    private List<gmfgraph_FigureAccessor> gmfgraph_figureaccessors;




    private gmfgraph_FigureAccessor gmfgraph_figureaccessor;


    public gmfgraph_CustomFigure(
    ) {
        super(
        );
        this.gmfgraph_figureaccessors = new ArrayList<>();
    }

    public gmfgraph_CustomFigure(
        ArrayList<gmfgraph_FigureAccessor> gmfgraph_figureaccessors    ) {
        this.gmfgraph_figureaccessors = gmfgraph_figureaccessors;
    }


    public List<gmfgraph_FigureAccessor> getGmfgraph_figureaccessors() {
        return gmfgraph_figureaccessors;
    }

    public void addGmfgraph_figureaccessor(Gmfgraph_figureaccessor gmfgraph_figureaccessor) {
        this.gmfgraph_figureaccessors.add(gmfgraph_figureaccessor);
    }
    public gmfgraph_FigureAccessor getGmfgraph_figureaccessor() {
        return gmfgraph_figureaccessor;
    }

    public void setGmfgraph_figureaccessor(gmfgraph_FigureAccessor gmfgraph_figureaccessor) {
        this.gmfgraph_figureaccessor = gmfgraph_figureaccessor;
    }

}