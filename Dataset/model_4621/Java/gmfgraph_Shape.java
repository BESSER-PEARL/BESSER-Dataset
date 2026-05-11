





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends RealFigure {

    private boolean fill;
    private boolean xorOutline;
    private boolean outline;
    private String lineKind;
    private boolean xorFill;
    private int lineWidth;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        boolean fill,        boolean xorOutline,        boolean outline,        String lineKind,        boolean xorFill,        int lineWidth    ) {
        super(
        );
        this.fill = fill;
        this.xorOutline = xorOutline;
        this.outline = outline;
        this.lineKind = lineKind;
        this.xorFill = xorFill;
        this.lineWidth = lineWidth;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        boolean fill,        boolean xorOutline,        boolean outline,        String lineKind,        boolean xorFill,        int lineWidth        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.fill = fill;
        this.xorOutline = xorOutline;
        this.outline = outline;
        this.lineKind = lineKind;
        this.xorFill = xorFill;
        this.lineWidth = lineWidth;
        this.gmfgraph_figures = gmfgraph_figures;
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
    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
    }
    public String getLinekind() {
        return lineKind;
    }

    public void setLinekind(String lineKind) {
        this.lineKind = lineKind;
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

    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }

}