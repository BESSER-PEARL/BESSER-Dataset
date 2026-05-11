





import java.util.List;
import java.util.ArrayList;

public class diagram_Ellipse extends NodeStyle {

    private String horizontalDiameter;
    private String color;
    private String verticalDiameter;



    public diagram_Ellipse(
        String horizontalDiameter,        String color,        String verticalDiameter    ) {
        super(
        );
        this.horizontalDiameter = horizontalDiameter;
        this.color = color;
        this.verticalDiameter = verticalDiameter;
    }


    public String getHorizontaldiameter() {
        return horizontalDiameter;
    }

    public void setHorizontaldiameter(String horizontalDiameter) {
        this.horizontalDiameter = horizontalDiameter;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getVerticaldiameter() {
        return verticalDiameter;
    }

    public void setVerticaldiameter(String verticalDiameter) {
        this.verticalDiameter = verticalDiameter;
    }


}