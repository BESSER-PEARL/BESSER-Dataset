





import java.util.List;
import java.util.ArrayList;

public class diagram_style_BorderedStyleDescription extends StyleDescription {

    private String borderSizeComputationExpression;
    private String borderLineStyle;



    public diagram_style_BorderedStyleDescription(
        String borderSizeComputationExpression,        String borderLineStyle    ) {
        super(
        );
        this.borderSizeComputationExpression = borderSizeComputationExpression;
        this.borderLineStyle = borderLineStyle;
    }


    public String getBordersizecomputationexpression() {
        return borderSizeComputationExpression;
    }

    public void setBordersizecomputationexpression(String borderSizeComputationExpression) {
        this.borderSizeComputationExpression = borderSizeComputationExpression;
    }
    public String getBorderlinestyle() {
        return borderLineStyle;
    }

    public void setBorderlinestyle(String borderLineStyle) {
        this.borderLineStyle = borderLineStyle;
    }


}