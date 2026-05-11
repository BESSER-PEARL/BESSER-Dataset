





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Figure extends FigureMarker, Identity, FigureHandle {






    private gmfgraph_Dimension gmfgraph_dimension;




    private gmfgraph_Dimension gmfgraph_dimension;




    private gmfgraph_Dimension gmfgraph_dimension;




    private gmfgraph_FigureRef gmfgraph_figureref;




    private List<gmfgraph_FigureMarker> gmfgraph_figuremarkers;




    private gmfgraph_FigureMarker gmfgraph_figuremarker;


    public gmfgraph_Figure(
    ) {
        super(
        );
        this.gmfgraph_figuremarkers = new ArrayList<>();
    }

    public gmfgraph_Figure(
        ArrayList<gmfgraph_FigureMarker> gmfgraph_figuremarkers    ) {
        this.gmfgraph_figuremarkers = gmfgraph_figuremarkers;
    }


    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }
    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }
    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }
    public gmfgraph_FigureRef getGmfgraph_figureref() {
        return gmfgraph_figureref;
    }

    public void setGmfgraph_figureref(gmfgraph_FigureRef gmfgraph_figureref) {
        this.gmfgraph_figureref = gmfgraph_figureref;
    }
    public List<gmfgraph_FigureMarker> getGmfgraph_figuremarkers() {
        return gmfgraph_figuremarkers;
    }

    public void addGmfgraph_figuremarker(Gmfgraph_figuremarker gmfgraph_figuremarker) {
        this.gmfgraph_figuremarkers.add(gmfgraph_figuremarker);
    }
    public gmfgraph_FigureMarker getGmfgraph_figuremarker() {
        return gmfgraph_figuremarker;
    }

    public void setGmfgraph_figuremarker(gmfgraph_FigureMarker gmfgraph_figuremarker) {
        this.gmfgraph_figuremarker = gmfgraph_figuremarker;
    }

}