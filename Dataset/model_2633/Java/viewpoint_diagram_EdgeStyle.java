





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_EdgeStyle extends Style {

    private String sourceArrow;
    private String routingStyle;
    private String foldingStyle;
    private String size;
    private String lineStyle;
    private String targetArrow;





    private diagram_viewpoint_RGBValues diagram_viewpoint_rgbvalues;


    public viewpoint_diagram_EdgeStyle(
        String sourceArrow,        String routingStyle,        String foldingStyle,        String size,        String lineStyle,        String targetArrow    ) {
        super(
        );
        this.sourceArrow = sourceArrow;
        this.routingStyle = routingStyle;
        this.foldingStyle = foldingStyle;
        this.size = size;
        this.lineStyle = lineStyle;
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

    public diagram_viewpoint_RGBValues getDiagram_viewpoint_rgbvalues() {
        return diagram_viewpoint_rgbvalues;
    }

    public void setDiagram_viewpoint_rgbvalues(diagram_viewpoint_RGBValues diagram_viewpoint_rgbvalues) {
        this.diagram_viewpoint_rgbvalues = diagram_viewpoint_rgbvalues;
    }

}