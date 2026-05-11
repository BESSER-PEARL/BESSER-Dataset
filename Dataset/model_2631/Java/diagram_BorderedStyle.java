





import java.util.List;
import java.util.ArrayList;

public class diagram_BorderedStyle extends Style {

    private String borderSizeComputationExpression;
    private String borderSize;



    public diagram_BorderedStyle(
        String borderSizeComputationExpression,        String borderSize    ) {
        super(
        );
        this.borderSizeComputationExpression = borderSizeComputationExpression;
        this.borderSize = borderSize;
    }


    public String getBordersizecomputationexpression() {
        return borderSizeComputationExpression;
    }

    public void setBordersizecomputationexpression(String borderSizeComputationExpression) {
        this.borderSizeComputationExpression = borderSizeComputationExpression;
    }
    public String getBordersize() {
        return borderSize;
    }

    public void setBordersize(String borderSize) {
        this.borderSize = borderSize;
    }


}