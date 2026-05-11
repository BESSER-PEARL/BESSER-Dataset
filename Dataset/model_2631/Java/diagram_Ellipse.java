





import java.util.List;
import java.util.ArrayList;

public class diagram_Ellipse extends NodeStyle {

    private String horizontalDiameter;
    private String verticalDiameter;



    public diagram_Ellipse(
        String horizontalDiameter,        String verticalDiameter    ) {
        super(
        );
        this.horizontalDiameter = horizontalDiameter;
        this.verticalDiameter = verticalDiameter;
    }


    public String getHorizontaldiameter() {
        return horizontalDiameter;
    }

    public void setHorizontaldiameter(String horizontalDiameter) {
        this.horizontalDiameter = horizontalDiameter;
    }
    public String getVerticaldiameter() {
        return verticalDiameter;
    }

    public void setVerticaldiameter(String verticalDiameter) {
        this.verticalDiameter = verticalDiameter;
    }


}