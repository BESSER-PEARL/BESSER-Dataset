





import java.util.List;
import java.util.ArrayList;

public class diagram_Ellipse extends NodeStyle {

    private String horizontalDiameter;
    private String verticalDiameter;
    private String color;



    public diagram_Ellipse(
        String horizontalDiameter,        String verticalDiameter,        String color    ) {
        super(
        );
        this.horizontalDiameter = horizontalDiameter;
        this.verticalDiameter = verticalDiameter;
        this.color = color;
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
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}