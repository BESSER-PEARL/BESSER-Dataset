





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_ComputedColor extends description_UserColor, description_ColorDescription {

    private String green;
    private String blue;
    private String red;



    public viewpoint_description_ComputedColor(
        String green,        String blue,        String red    ) {
        super(
        );
        this.green = green;
        this.blue = blue;
        this.red = red;
    }


    public String getGreen() {
        return green;
    }

    public void setGreen(String green) {
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


}