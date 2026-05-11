





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FigureAccessor  {

    private String accessor;





    private gmfgraph_RealFigure gmfgraph_realfigure;




    private gmfgraph_CustomFigure gmfgraph_customfigure;


    public gmfgraph_FigureAccessor(
        String accessor    ) {
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }

    public gmfgraph_RealFigure getGmfgraph_realfigure() {
        return gmfgraph_realfigure;
    }

    public void setGmfgraph_realfigure(gmfgraph_RealFigure gmfgraph_realfigure) {
        this.gmfgraph_realfigure = gmfgraph_realfigure;
    }
    public gmfgraph_CustomFigure getGmfgraph_customfigure() {
        return gmfgraph_customfigure;
    }

    public void setGmfgraph_customfigure(gmfgraph_CustomFigure gmfgraph_customfigure) {
        this.gmfgraph_customfigure = gmfgraph_customfigure;
    }

}