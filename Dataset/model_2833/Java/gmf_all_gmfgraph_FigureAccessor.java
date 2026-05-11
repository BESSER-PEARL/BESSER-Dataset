





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_FigureAccessor  {

    private String accessor;





    private RealFigure realfigure;


    public gmf_all_gmfgraph_FigureAccessor(
        String accessor    ) {
        this.accessor = accessor;
    }


    public String getAccessor() {
        return accessor;
    }

    public void setAccessor(String accessor) {
        this.accessor = accessor;
    }

    public RealFigure getRealfigure() {
        return realfigure;
    }

    public void setRealfigure(RealFigure realfigure) {
        this.realfigure = realfigure;
    }

}