





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends Figure {

    private boolean xorOutline;
    private String lineKind;
    private boolean fill;
    private boolean outline;
    private int lineWidth;
    private boolean xorFill;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        boolean xorOutline,        String lineKind,        boolean fill,        boolean outline,        int lineWidth,        boolean xorFill    ) {
        super(
        );
        this.xorOutline = xorOutline;
        this.lineKind = lineKind;
        this.fill = fill;
        this.outline = outline;
        this.lineWidth = lineWidth;
        this.xorFill = xorFill;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        boolean xorOutline,        String lineKind,        boolean fill,        boolean outline,        int lineWidth,        boolean xorFill        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.xorOutline = xorOutline;
        this.lineKind = lineKind;
        this.fill = fill;
        this.outline = outline;
        this.lineWidth = lineWidth;
        this.xorFill = xorFill;
        this.gmfgraph_figures = gmfgraph_figures;
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
    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
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
    public boolean getXorfill() {
        return xorFill;
    }

    public void setXorfill(boolean xorFill) {
        this.xorFill = xorFill;
    }

    public List<gmfgraph_Figure> getGmfgraph_figures() {
        return gmfgraph_figures;
    }

    public void addGmfgraph_figure(Gmfgraph_figure gmfgraph_figure) {
        this.gmfgraph_figures.add(gmfgraph_figure);
    }

}