





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends RealFigure {

    private int lineWidth;
    private String lineKind;
    private boolean fill;
    private boolean xorFill;
    private boolean xorOutline;
    private boolean outline;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        int lineWidth,        String lineKind,        boolean fill,        boolean xorFill,        boolean xorOutline,        boolean outline    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.lineKind = lineKind;
        this.fill = fill;
        this.xorFill = xorFill;
        this.xorOutline = xorOutline;
        this.outline = outline;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        int lineWidth,        String lineKind,        boolean fill,        boolean xorFill,        boolean xorOutline,        boolean outline        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.lineWidth = lineWidth;
        this.lineKind = lineKind;
        this.fill = fill;
        this.xorFill = xorFill;
        this.xorOutline = xorOutline;
        this.outline = outline;
        this.gmfgraph_figures = gmfgraph_figures;
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
    public boolean getXoroutline() {
        return xorOutline;
    }

    public void setXoroutline(boolean xorOutline) {
        this.xorOutline = xorOutline;
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