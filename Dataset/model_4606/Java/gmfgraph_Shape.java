





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends RealFigure {

    private boolean xorFill;
    private boolean outline;
    private boolean fill;
    private int lineWidth;
    private String lineKind;
    private boolean xorOutline;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        boolean xorFill,        boolean outline,        boolean fill,        int lineWidth,        String lineKind,        boolean xorOutline    ) {
        super(
        );
        this.xorFill = xorFill;
        this.outline = outline;
        this.fill = fill;
        this.lineWidth = lineWidth;
        this.lineKind = lineKind;
        this.xorOutline = xorOutline;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        boolean xorFill,        boolean outline,        boolean fill,        int lineWidth,        String lineKind,        boolean xorOutline        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.xorFill = xorFill;
        this.outline = outline;
        this.fill = fill;
        this.lineWidth = lineWidth;
        this.lineKind = lineKind;
        this.xorOutline = xorOutline;
        this.gmfgraph_figures = gmfgraph_figures;
    }

    public boolean getXorfill() {
        return xorFill;
    }

    public void setXorfill(boolean xorFill) {
        this.xorFill = xorFill;
    }
    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public String getLinekind() {
        return lineKind;
    }

    public void setLinekind(String lineKind) {
        this.lineKind = lineKind;
    }
    public boolean getXoroutline() {
        return xorOutline;
    }

    public void setXoroutline(boolean xorOutline) {
        this.xorOutline = xorOutline;
    }

    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }

}