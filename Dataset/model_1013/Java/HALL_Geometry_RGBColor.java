





import java.util.List;
import java.util.ArrayList;

public class HALL_Geometry_RGBColor  {

    private int blueValue;
    private int redValue;
    private int greenValue;



    public HALL_Geometry_RGBColor(
        int blueValue,        int redValue,        int greenValue    ) {
        this.blueValue = blueValue;
        this.redValue = redValue;
        this.greenValue = greenValue;
    }


    public int getBluevalue() {
        return blueValue;
    }

    public void setBluevalue(int blueValue) {
        this.blueValue = blueValue;
    }
    public int getRedvalue() {
        return redValue;
    }

    public void setRedvalue(int redValue) {
        this.redValue = redValue;
    }
    public int getGreenvalue() {
        return greenValue;
    }

    public void setGreenvalue(int greenValue) {
        this.greenValue = greenValue;
    }


}