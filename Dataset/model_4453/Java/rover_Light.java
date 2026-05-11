





import java.util.List;
import java.util.ArrayList;

public class rover_Light extends Actuator {

    private String color;





    private rover_SetLightColor rover_setlightcolor;


    public rover_Light(
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

    public rover_SetLightColor getRover_setlightcolor() {
        return rover_setlightcolor;
    }

    public void setRover_setlightcolor(rover_SetLightColor rover_setlightcolor) {
        this.rover_setlightcolor = rover_setlightcolor;
    }

}