





import java.util.List;
import java.util.ArrayList;

public class diagram_EdgeStyle extends Style {

    private String centered;
    private String strokeColor;
    private String lineStyle;
    private String targetArrow;
    private String sourceArrow;
    private String routingStyle;
    private String foldingStyle;
    private String size;





    private diagram_DEdge diagram_dedge;


    public diagram_EdgeStyle(
        String centered,        String strokeColor,        String lineStyle,        String targetArrow,        String sourceArrow,        String routingStyle,        String foldingStyle,        String size    ) {
        super(
        );
        this.centered = centered;
        this.strokeColor = strokeColor;
        this.lineStyle = lineStyle;
        this.targetArrow = targetArrow;
        this.sourceArrow = sourceArrow;
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.size = size;
    }


    public String getCentered() {
        return centered;
    }

    public void setCentered(String centered) {
        this.centered = centered;
    }
    public String getStrokecolor() {
        return strokeColor;
    }

    public void setStrokecolor(String strokeColor) {
        this.strokeColor = strokeColor;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
    }
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public String getFoldingstyle() {
        return foldingStyle;
    }

    public void setFoldingstyle(String foldingStyle) {
        this.foldingStyle = foldingStyle;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public diagram_DEdge getDiagram_dedge() {
        return diagram_dedge;
    }

    public void setDiagram_dedge(diagram_DEdge diagram_dedge) {
        this.diagram_dedge = diagram_dedge;
    }

}