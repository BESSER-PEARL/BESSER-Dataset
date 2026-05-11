





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends RealFigure {

    private boolean outline;
    private int lineWidth;
    private boolean xorOutline;
    private boolean fill;
    private boolean xorFill;
    private String lineKind;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        boolean outline,        int lineWidth,        boolean xorOutline,        boolean fill,        boolean xorFill,        String lineKind    ) {
        super(
        );
        this.outline = outline;
        this.lineWidth = lineWidth;
        this.xorOutline = xorOutline;
        this.fill = fill;
        this.xorFill = xorFill;
        this.lineKind = lineKind;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        boolean outline,        int lineWidth,        boolean xorOutline,        boolean fill,        boolean xorFill,        String lineKind        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.outline = outline;
        this.lineWidth = lineWidth;
        this.xorOutline = xorOutline;
        this.fill = fill;
        this.xorFill = xorFill;
        this.lineKind = lineKind;
        this.gmfgraph_figures = gmfgraph_figures;
    }

    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public boolean getXoroutline() {
        return xorOutline;
    }

    public void setXoroutline(boolean xorOutline) {
        this.xorOutline = xorOutline;
    }
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
    }
    public boolean getXorfill() {
        return xorFill;
    }

    public void setXorfill(boolean xorFill) {
        this.xorFill = xorFill;
    }
    public String getLinekind() {
        return lineKind;
    }

    public void setLinekind(String lineKind) {
        this.lineKind = lineKind;
    }

    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }

}