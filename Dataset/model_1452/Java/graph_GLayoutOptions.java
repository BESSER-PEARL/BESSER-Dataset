





import java.util.List;
import java.util.ArrayList;

public class graph_GLayoutOptions  {

    private String paddingTop;
    private String paddingRight;
    private boolean resizeContainer;
    private String hGap;
    private String vGap;
    private String minWidth;
    private String paddingLeft;
    private String hAlign;
    private String vAlign;
    private String paddingBottom;
    private String paddingFactor;
    private String minHeight;





    private graph_GGraph graph_ggraph;


    public graph_GLayoutOptions(
        String paddingTop,        String paddingRight,        boolean resizeContainer,        String hGap,        String vGap,        String minWidth,        String paddingLeft,        String hAlign,        String vAlign,        String paddingBottom,        String paddingFactor,        String minHeight    ) {
        this.paddingTop = paddingTop;
        this.paddingRight = paddingRight;
        this.resizeContainer = resizeContainer;
        this.hGap = hGap;
        this.vGap = vGap;
        this.minWidth = minWidth;
        this.paddingLeft = paddingLeft;
        this.hAlign = hAlign;
        this.vAlign = vAlign;
        this.paddingBottom = paddingBottom;
        this.paddingFactor = paddingFactor;
        this.minHeight = minHeight;
    }


    public String getPaddingtop() {
        return paddingTop;
    }

    public void setPaddingtop(String paddingTop) {
        this.paddingTop = paddingTop;
    }
    public String getPaddingright() {
        return paddingRight;
    }

    public void setPaddingright(String paddingRight) {
        this.paddingRight = paddingRight;
    }
    public boolean getResizecontainer() {
        return resizeContainer;
    }

    public void setResizecontainer(boolean resizeContainer) {
        this.resizeContainer = resizeContainer;
    }
    public String getHgap() {
        return hGap;
    }

    public void setHgap(String hGap) {
        this.hGap = hGap;
    }
    public String getVgap() {
        return vGap;
    }

    public void setVgap(String vGap) {
        this.vGap = vGap;
    }
    public String getMinwidth() {
        return minWidth;
    }

    public void setMinwidth(String minWidth) {
        this.minWidth = minWidth;
    }
    public String getPaddingleft() {
        return paddingLeft;
    }

    public void setPaddingleft(String paddingLeft) {
        this.paddingLeft = paddingLeft;
    }
    public String getHalign() {
        return hAlign;
    }

    public void setHalign(String hAlign) {
        this.hAlign = hAlign;
    }
    public String getValign() {
        return vAlign;
    }

    public void setValign(String vAlign) {
        this.vAlign = vAlign;
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