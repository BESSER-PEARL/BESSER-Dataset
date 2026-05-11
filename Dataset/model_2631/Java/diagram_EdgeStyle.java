





import java.util.List;
import java.util.ArrayList;

public class diagram_EdgeStyle extends Style {

    private String lineStyle;
    private String size;
    private String foldingStyle;
    private String sourceArrow;
    private String routingStyle;
    private String targetArrow;





    private diagram_DEdge diagram_dedge;


    public diagram_EdgeStyle(
        String lineStyle,        String size,        String foldingStyle,        String sourceArrow,        String routingStyle,        String targetArrow    ) {
        super(
        );
        this.lineStyle = lineStyle;
        this.size = size;
        this.foldingStyle = foldingStyle;
        this.sourceArrow = sourceArrow;
        this.routingStyle = routingStyle;
        this.targetArrow = targetArrow;
    }


    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
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

    public diagram_DEdge getDiagram_dedge() {
        return diagram_dedge;
    }

    public void setDiagram_dedge(diagram_DEdge diagram_dedge) {
        this.diagram_dedge = diagram_dedge;
    }

}