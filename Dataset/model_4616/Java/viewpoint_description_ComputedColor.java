





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_ComputedColor extends description_ColorDescription, description_UserColor {

    private String red;
    private String blue;
    private String green;



    public viewpoint_description_ComputedColor(
        String red,        String blue,        String green    ) {
        super(
        );
        this.red = red;
        this.blue = blue;
        this.green = green;
    }


    public String getRed() {
        return red;
    }

    public void setRed(String red) {
        this.red = red;
    }
    public String getBlue() {
        return blue;
    }

    public void setBlue(String blue) {
        this.blue = blue;
    }
    public String getGreen() {
        return green;
    }

    public void setGreen(String green) {
        this.green = green;
    }


}