





import java.util.List;
import java.util.ArrayList;

public class roverml_SetLightColor extends Command {

    private String color;



    public roverml_SetLightColor(
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