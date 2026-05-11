





import java.util.List;
import java.util.ArrayList;

public class diagram_BorderedStyle extends Style {

    private String borderSize;
    private String borderSizeComputationExpression;
    private String borderColor;
    private String borderLineStyle;



    public diagram_BorderedStyle(
        String borderSize,        String borderSizeComputationExpression,        String borderColor,        String borderLineStyle    ) {
        super(
        );
        this.borderSize = borderSize;
        this.borderSizeComputationExpression = borderSizeComputationExpression;
        this.borderColor = borderColor;
        this.borderLineStyle = borderLineStyle;
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
    public String getBordercolor() {
        return borderColor;
    }

    public void setBordercolor(String borderColor) {
        this.borderColor = borderColor;
    }
    public String getBorderlinestyle() {
        return borderLineStyle;
    }

    public void setBorderlinestyle(String borderLineStyle) {
        this.borderLineStyle = borderLineStyle;
    }


}