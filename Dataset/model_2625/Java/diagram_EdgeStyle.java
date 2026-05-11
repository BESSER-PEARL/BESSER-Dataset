





import java.util.List;
import java.util.ArrayList;

public class diagram_EdgeStyle extends Style {

    private String foldingStyle;
    private String size;
    private String routingStyle;
    private String centered;
    private String lineStyle;
    private String sourceArrow;
    private String strokeColor;
    private String targetArrow;





    private diagram_DEdge diagram_dedge;


    public diagram_EdgeStyle(
        String foldingStyle,        String size,        String routingStyle,        String centered,        String lineStyle,        String sourceArrow,        String strokeColor,        String targetArrow    ) {
        super(
        );
        this.foldingStyle = foldingStyle;
        this.size = size;
        this.routingStyle = routingStyle;
        this.centered = centered;
        this.lineStyle = lineStyle;
        this.sourceArrow = sourceArrow;
        this.strokeColor = strokeColor;
        this.targetArrow = targetArrow;
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
    public String getRoutingstyle() {
        return routingStyle;
    }

    public void setRoutingstyle(String routingStyle) {
        this.routingStyle = routingStyle;
    }
    public String getCentered() {
        return centered;
    }

    public void setCentered(String centered) {
        this.centered = centered;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getSourcearrow() {
        return sourceArrow;
    }

    public void setSourcearrow(String sourceArrow) {
        this.sourceArrow = sourceArrow;
    }
    public String getStrokecolor() {
        return strokeColor;
    }

    public void setStrokecolor(String strokeColor) {
        this.strokeColor = strokeColor;
    }
    public String getTargetarrow() {
        return targetArrow;
    }

    public void setTargetarrow(String targetArrow) {
        this.targetArrow = targetArrow;
    }

    public diagram_DEdge getDiagram_dedge() {
        return diagram_dedge;
    }

    public void setDiagram_dedge(diagram_DEdge diagram_dedge) {
        this.diagram_dedge = diagram_dedge;
    }

}