





import java.util.List;
import java.util.ArrayList;

public class diagram_BorderedStyle extends Style {

    private String borderSize;
    private String borderColor;
    private String borderSizeComputationExpression;
    private String borderLineStyle;



    public diagram_BorderedStyle(
        String borderSize,        String borderColor,        String borderSizeComputationExpression,        String borderLineStyle    ) {
        super(
        );
        this.borderSize = borderSize;
        this.borderColor = borderColor;
        this.borderSizeComputationExpression = borderSizeComputationExpression;
        this.borderLineStyle = borderLineStyle;
    }


    public String getBordersize() {
        return borderSize;
    }

    public void setBordersize(String borderSize) {
        this.borderSize = borderSize;
    }
    public String getBordercolor() {
        return borderColor;
    }

    public void setBordercolor(String borderColor) {
        this.borderColor = borderColor;
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