





import java.util.List;
import java.util.ArrayList;

public class HALL_Geometry_RGBColor  {

    private int greenValue;
    private int redValue;
    private int blueValue;



    public HALL_Geometry_RGBColor(
        int greenValue,        int redValue,        int blueValue    ) {
        this.greenValue = greenValue;
        this.redValue = redValue;
        this.blueValue = blueValue;
    }


    public int getGreenvalue() {
        return greenValue;
    }

    public void setGreenvalue(int greenValue) {
        this.greenValue = greenValue;
    }
    public int getRedvalue() {
        return redValue;
    }

    public void setRedvalue(int redValue) {
        this.redValue = redValue;
    }
    public int getBluevalue() {
        return blueValue;
    }

    public void setBluevalue(int blueValue) {
        this.blueValue = blueValue;
    }


}