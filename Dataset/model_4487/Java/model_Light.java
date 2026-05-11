





import java.util.List;
import java.util.ArrayList;

public class model_Light extends Command {

    private String color;



    public model_Light(
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