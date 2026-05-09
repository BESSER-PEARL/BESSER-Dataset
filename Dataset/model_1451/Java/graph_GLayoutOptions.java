





import java.util.List;
import java.util.ArrayList;

public class graph_GLayoutOptions  {

    private boolean resizeContainer;
    private String paddingLeft;
    private String vGap;
    private String hAlign;
    private String hGap;
    private String paddingFactor;
    private String minHeight;
    private String minWidth;
    private String paddingTop;
    private String paddingBottom;
    private String paddingRight;
    private String vAlign;





    private graph_GGraph graph_ggraph;


    public graph_GLayoutOptions(
        boolean resizeContainer,        String paddingLeft,        String vGap,        String hAlign,        String hGap,        String paddingFactor,        String minHeight,        String minWidth,        String paddingTop,        String paddingBottom,        String paddingRight,        String vAlign    ) {
        this.resizeContainer = resizeContainer;
        this.paddingLeft = paddingLeft;
        this.vGap = vGap;
        this.hAlign = hAlign;
        this.hGap = hGap;
        this.paddingFactor = paddingFactor;
        this.minHeight = minHeight;
        this.minWidth = minWidth;
        this.paddingTop = paddingTop;
        this.paddingBottom = paddingBottom;
        this.paddingRight = paddingRight;
        this.vAlign = vAlign;
    }


    public boolean getResizecontainer() {
        return resizeContainer;
    }

    public void setResizecontainer(boolean resizeContainer) {
        this.resizeContainer = resizeContainer;
    }
    public String getPaddingleft() {
        return paddingLeft;
    }

    public void setPaddingleft(String paddingLeft) {
        this.paddingLeft = paddingLeft;
    }
    public String getVgap() {
        return vGap;
    }

    public void setVgap(String vGap) {
        this.vGap = vGap;
    }
    public String getHalign() {
        return hAlign;
    }

    public void setHalign(String hAlign) {
        this.hAlign = hAlign;
    }
    public String getHgap() {
        return hGap;
    }

    public void setHgap(String hGap) {
        this.hGap = hGap;
    }
    public String getPaddingfactor() {
        return paddingFactor;
    }

    public void setPaddingfactor(String paddingFactor) {
        this.paddingFactor = paddingFactor;
    }
    public String getMinheight() {
        return minHeight;
    }

    public void setMinheight(String minHeight) {
        this.minHeight = minHeight;
    }
    public String getMinwidth() {
        return minWidth;
    }

    public void setMinwidth(String minWidth) {
        this.minWidth = minWidth;
    }
    public String getPaddingtop() {
        return paddingTop;
    }

    public void setPaddingtop(String paddingTop) {
        this.paddingTop = paddingTop;
    }
    public String getPaddingbottom() {
        return paddingBottom;
    }

    public void setPaddingbottom(String paddingBottom) {
        this.paddingBottom = paddingBottom;
    }
    public String getPaddingright() {
        return paddingRight;
    }

    public void setPaddingright(String paddingRight) {
        this.paddingRight = paddingRight;
    }
    public String getValign() {
        return vAlign;
    }

    public void setValign(String vAlign) {
        this.vAlign = vAlign;
    }

    public graph_GGraph getGraph_ggraph() {
        return graph_ggraph;
    }

    public void setGraph_ggraph(graph_GGraph graph_ggraph) {
        this.graph_ggraph = graph_ggraph;
    }

}