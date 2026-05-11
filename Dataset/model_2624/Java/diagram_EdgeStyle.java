





import java.util.List;
import java.util.ArrayList;

public class diagram_EdgeStyle extends Style {

    private String foldingStyle;
    private String routingStyle;
    private String targetArrow;
    private String size;
    private String centered;
    private String strokeColor;
    private String sourceArrow;
    private String lineStyle;





    private diagram_DEdge diagram_dedge;


    public diagram_EdgeStyle(
        String foldingStyle,        String routingStyle,        String targetArrow,        String size,        String centered,        String strokeColor,        String sourceArrow,        String lineStyle    ) {
        super(
        );
        this.foldingStyle = foldingStyle;
        this.routingStyle = routingStyle;
        this.targetArrow = targetArrow;
        this.size = size;
        this.centered = centered;
        this.strokeColor = strokeColor;
        this.sourceArrow = sourceArrow;
        this.lineStyle = lineStyle;
    }


    public String getFoldingstyle() {
        return foldingStyle;
    }

    public void setFoldingstyle(String foldingStyle) {
        this.foldingStyle = foldingStyle;
    }
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
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
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }

    public diagram_DEdge getDiagram_dedge() {
        return diagram_dedge;
    }

    public void setDiagram_dedge(diagram_DEdge diagram_dedge) {
        this.diagram_dedge = diagram_dedge;
    }

}