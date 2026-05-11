





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Shape extends Figure {

    private boolean fill;
    private String lineKind;
    private boolean xorOutline;
    private int lineWidth;
    private boolean outline;
    private boolean xorFill;





    private List<gmfgraph_Figure> gmfgraph_figures;


    public gmfgraph_Shape(
        boolean fill,        String lineKind,        boolean xorOutline,        int lineWidth,        boolean outline,        boolean xorFill    ) {
        super(
        );
        this.fill = fill;
        this.lineKind = lineKind;
        this.xorOutline = xorOutline;
        this.lineWidth = lineWidth;
        this.outline = outline;
        this.xorFill = xorFill;
        this.gmfgraph_figures = new ArrayList<>();
    }

    public gmfgraph_Shape(
        boolean fill,        String lineKind,        boolean xorOutline,        int lineWidth,        boolean outline,        boolean xorFill        ArrayList<gmfgraph_Figure> gmfgraph_figures    ) {
        this.fill = fill;
        this.lineKind = lineKind;
        this.xorOutline = xorOutline;
        this.lineWidth = lineWidth;
        this.outline = outline;
        this.xorFill = xorFill;
        this.gmfgraph_figures = gmfgraph_figures;
    }

    public boolean getFill() {
        return fill;
    }

    public void setFill(boolean fill) {
        this.fill = fill;
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
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }
    public boolean getOutline() {
        return outline;
    }

    public void setOutline(boolean outline) {
        this.outline = outline;
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