





import java.util.List;
import java.util.ArrayList;

public class rover_SetLightColor extends Command {

    private String lightColor;





    private rover_Repeat rover_repeat;


    public rover_SetLightColor(
        String lightColor    ) {
        super(
        );
        this.lightColor = lightColor;
    }


    public String getLightcolor() {
        return lightColor;
    }

    public void setLightcolor(String lightColor) {
        this.lightColor = lightColor;
    }

    public rover_Repeat getRover_repeat() {
        return rover_repeat;
    }

    public void setRover_repeat(rover_Repeat rover_repeat) {
        this.rover_repeat = rover_repeat;
    }

}