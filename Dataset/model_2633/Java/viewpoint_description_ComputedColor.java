





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_ComputedColor extends description_ColorDescription, description_UserColor {

    private String blue;
    private String red;
    private String green;



    public viewpoint_description_ComputedColor(
        String blue,        String red,        String green    ) {
        super(
        );
        this.blue = blue;
        this.red = red;
        this.green = green;
    }


    public String getBlue() {
        return blue;
    }

    public void setBlue(String blue) {
        this.blue = blue;
    }
    public String getRed() {
        return red;
    }

    public void setRed(String red) {
        this.red = red;
    }
    public String getGreen() {
        return green;
    }

    public void setGreen(String green) {
        this.green = green;
    }


}