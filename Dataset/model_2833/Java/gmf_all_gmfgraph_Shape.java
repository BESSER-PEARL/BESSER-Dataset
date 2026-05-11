





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_Shape extends RealFigure {

    private boolean xorFill;
    private String lineKind;
    private boolean xorOutline;
    private boolean fill;
    private int lineWidth;
    private boolean outline;



    public gmf_all_gmfgraph_Shape(
        boolean xorFill,        String lineKind,        boolean xorOutline,        boolean fill,        int lineWidth,        boolean outline    ) {
        super(
        );
        this.xorFill = xorFill;
        this.lineKind = lineKind;
        this.xorOutline = xorOutline;
        this.fill = fill;
        this.lineWidth = lineWidth;
        this.outline = outline;
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


}