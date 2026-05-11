





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_RealFigure extends AbstractFigure {

    private String name;





    private List<gmfgraph_Figure> gmfgraph_figures;




    private gmfgraph_FigureRef gmfgraph_figureref;




    private gmfgraph_FigureAccessor gmfgraph_figureaccessor;


    public gmfgraph_RealFigure(
        String name    ) {
        super(
        );
        this.name = name;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_RealFigure(
        String name        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.name = name;
        this.gmfgraph_figures = gmfgraph_figures;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }
    public gmfgraph_FigureRef getGmfgraph_figureref() {
        return gmfgraph_figureref;
    }

    public void setGmfgraph_figureref(gmfgraph_FigureRef gmfgraph_figureref) {
        this.gmfgraph_figureref = gmfgraph_figureref;
    }
    public gmfgraph_FigureAccessor getGmfgraph_figureaccessor() {
        return gmfgraph_figureaccessor;
    }

    public void setGmfgraph_figureaccessor(gmfgraph_FigureAccessor gmfgraph_figureaccessor) {
        this.gmfgraph_figureaccessor = gmfgraph_figureaccessor;
    }

}