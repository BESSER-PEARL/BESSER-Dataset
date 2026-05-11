





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_BorderedStyle extends Style {

    private String borderSize;
    private String borderSizeComputationExpression;





    private diagram_viewpoint_RGBValues diagram_viewpoint_rgbvalues;


    public viewpoint_diagram_BorderedStyle(
        String borderSize,        String borderSizeComputationExpression    ) {
        super(
        );
        this.borderSize = borderSize;
        this.borderSizeComputationExpression = borderSizeComputationExpression;
    }


    public String getBordersize() {
        return borderSize;
    }

    public void setBordersize(String borderSize) {
        this.borderSize = borderSize;
    }
    public String getBordersizecomputationexpression() {
        return borderSizeComputationExpression;
    }

    public void setBordersizecomputationexpression(String borderSizeComputationExpression) {
        this.borderSizeComputationExpression = borderSizeComputationExpression;
    }

    public diagram_viewpoint_RGBValues getDiagram_viewpoint_rgbvalues() {
        return diagram_viewpoint_rgbvalues;
    }

    public void setDiagram_viewpoint_rgbvalues(diagram_viewpoint_RGBValues diagram_viewpoint_rgbvalues) {
        this.diagram_viewpoint_rgbvalues = diagram_viewpoint_rgbvalues;
    }

}