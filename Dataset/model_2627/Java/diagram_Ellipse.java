





import java.util.List;
import java.util.ArrayList;

public class diagram_Ellipse extends NodeStyle {

    private String verticalDiameter;
    private String horizontalDiameter;
    private String color;



    public diagram_Ellipse(
        String verticalDiameter,        String horizontalDiameter,        String color    ) {
        super(
        );
        this.verticalDiameter = verticalDiameter;
        this.horizontalDiameter = horizontalDiameter;
        this.color = color;
    }


    public String getVerticaldiameter() {
        return verticalDiameter;
    }

    public void setVerticaldiameter(String verticalDiameter) {
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


}