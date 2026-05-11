





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Node extends DiagramElement {

    private String resizeConstraint;
    private String affixedParentSide;





    private gmfgraph_Canvas gmfgraph_canvas;




    private gmfgraph_Figure gmfgraph_figure;


    public gmfgraph_Node(
        String resizeConstraint,        String affixedParentSide    ) {
        super(
        );
        this.resizeConstraint = resizeConstraint;
        this.affixedParentSide = affixedParentSide;
    }


    public String getResizeconstraint() {
        return resizeConstraint;
    }

    public void setResizeconstraint(String resizeConstraint) {
        this.resizeConstraint = resizeConstraint;
    }
    public String getAffixedparentside() {
        return affixedParentSide;
    }

    public void setAffixedparentside(String affixedParentSide) {
        this.affixedParentSide = affixedParentSide;
    }

    public gmfgraph_Canvas getGmfgraph_canvas() {
        return gmfgraph_canvas;
    }

    public void setGmfgraph_canvas(gmfgraph_Canvas gmfgraph_canvas) {
        this.gmfgraph_canvas = gmfgraph_canvas;
    }
    public gmfgraph_Figure getGmfgraph_figure() {
        return gmfgraph_figure;
    }

    public void setGmfgraph_figure(gmfgraph_Figure gmfgraph_figure) {
        this.gmfgraph_figure = gmfgraph_figure;
    }

}