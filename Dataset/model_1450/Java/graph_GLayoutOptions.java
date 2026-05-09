





import java.util.List;
import java.util.ArrayList;

public class graph_GLayoutOptions  {

    private String vAlign;
    private String vGap;
    private String hAlign;
    private String paddingRight;
    private String hGap;
    private String paddingBottom;
    private String paddingFactor;
    private String paddingLeft;
    private String minWidth;
    private String paddingTop;
    private boolean resizeContainer;
    private String minHeight;





    private graph_GGraph graph_ggraph;


    public graph_GLayoutOptions(
        String vAlign,        String vGap,        String hAlign,        String paddingRight,        String hGap,        String paddingBottom,        String paddingFactor,        String paddingLeft,        String minWidth,        String paddingTop,        boolean resizeContainer,        String minHeight    ) {
        this.vAlign = vAlign;
        this.vGap = vGap;
        this.hAlign = hAlign;
        this.paddingRight = paddingRight;
        this.hGap = hGap;
        this.paddingBottom = paddingBottom;
        this.paddingFactor = paddingFactor;
        this.paddingLeft = paddingLeft;
        this.minWidth = minWidth;
        this.paddingTop = paddingTop;
        this.resizeContainer = resizeContainer;
        this.minHeight = minHeight;
    }


    public String getValign() {
        return vAlign;
    }

    public void setValign(String vAlign) {
        this.vAlign = vAlign;
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
    public String getPaddingright() {
        return paddingRight;
    }

    public void setPaddingright(String paddingRight) {
        this.paddingRight = paddingRight;
    }
    public String getHgap() {
        return hGap;
    }

    public void setHgap(String hGap) {
        this.hGap = hGap;
    }
    public String getPaddingbottom() {
        return paddingBottom;
    }

    public void setPaddingbottom(String paddingBottom) {
        this.paddingBottom = paddingBottom;
    }
    public String getPaddingfactor() {
        return paddingFactor;
    }

    public void setPaddingfactor(String paddingFactor) {
        this.paddingFactor = paddingFactor;
    }
    public String getPaddingleft() {
        return paddingLeft;
    }

    public void setPaddingleft(String paddingLeft) {
        this.paddingLeft = paddingLeft;
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
    public boolean getResizecontainer() {
        return resizeContainer;
    }

    public void setResizecontainer(boolean resizeContainer) {
        this.resizeContainer = resizeContainer;
    }
    public String getMinheight() {
        return minHeight;
    }

    public void setMinheight(String minHeight) {
        this.minHeight = minHeight;
    }

    public graph_GGraph getGraph_ggraph() {
        return graph_ggraph;
    }

    public void setGraph_ggraph(graph_GGraph graph_ggraph) {
        this.graph_ggraph = graph_ggraph;
    }

}