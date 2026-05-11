





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends RealFigure {

    private boolean xorFill;
    private int lineWidth;
    private boolean fill;
    private boolean xorOutline;
    private String lineKind;
    private boolean outline;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        boolean xorFill,        int lineWidth,        boolean fill,        boolean xorOutline,        String lineKind,        boolean outline    ) {
        super(
        );
        this.xorFill = xorFill;
        this.lineWidth = lineWidth;
        this.fill = fill;
        this.xorOutline = xorOutline;
        this.lineKind = lineKind;
        this.outline = outline;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        boolean xorFill,        int lineWidth,        boolean fill,        boolean xorOutline,        String lineKind,        boolean outline        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.xorFill = xorFill;
        this.lineWidth = lineWidth;
        this.fill = fill;
        this.xorOutline = xorOutline;
        this.lineKind = lineKind;
        this.outline = outline;
        this.gmfgraph_figures = gmfgraph_figures;
    }

    public boolean getXorfill() {
        return xorFill;
    }

    public void setXorfill(boolean xorFill) {
        this.xorFill = xorFill;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
    }
    public boolean getXoroutline() {
        return xorOutline;
    }

    public void setXoroutline(boolean xorOutline) {
        this.xorOutline = xorOutline;
    }
    public String getLinekind() {
        return lineKind;
    }

    public void setLinekind(String lineKind) {
        this.lineKind = lineKind;
    }
    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }

    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }

}