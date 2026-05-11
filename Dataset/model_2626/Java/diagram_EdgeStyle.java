





import java.util.List;
import java.util.ArrayList;

public class diagram_EdgeStyle extends Style {

    private String lineStyle;
    private String centered;
    private String targetArrow;
    private String size;
    private String routingStyle;
    private String strokeColor;
    private String foldingStyle;
    private String sourceArrow;





    private diagram_DEdge diagram_dedge;


    public diagram_EdgeStyle(
        String lineStyle,        String centered,        String targetArrow,        String size,        String routingStyle,        String strokeColor,        String foldingStyle,        String sourceArrow    ) {
        super(
        );
        this.lineStyle = lineStyle;
        this.centered = centered;
        this.targetArrow = targetArrow;
        this.size = size;
        this.routingStyle = routingStyle;
        this.strokeColor = strokeColor;
        this.foldingStyle = foldingStyle;
        this.sourceArrow = sourceArrow;
    }


    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getCentered() {
        return centered;
    }

    public void setCentered(String centered) {
        this.centered = centered;
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
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public String getStrokecolor() {
        return strokeColor;
    }

    public void setStrokecolor(String strokeColor) {
        this.strokeColor = strokeColor;
    }
    public String getFoldingstyle() {
        return foldingStyle;
    }

    public void setFoldingstyle(String foldingStyle) {
        this.foldingStyle = foldingStyle;
    }
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }

    public diagram_DEdge getDiagram_dedge() {
        return diagram_dedge;
    }

    public void setDiagram_dedge(diagram_DEdge diagram_dedge) {
        this.diagram_dedge = diagram_dedge;
    }

}