





import java.util.List;
import java.util.ArrayList;

public class mindstorms_ColorSensor extends Sensor {

    private String color;



    public mindstorms_ColorSensor(
        String color    ) {
        super(
        );
        this.color = color;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}