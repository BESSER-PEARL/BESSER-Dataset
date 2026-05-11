





import java.util.List;
import java.util.ArrayList;

public class arduino_LED extends ArduinoDigitalModule {

    private String color;



    public arduino_LED(
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