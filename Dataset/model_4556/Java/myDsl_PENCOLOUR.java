





import java.util.List;
import java.util.ArrayList;

public class myDsl_PENCOLOUR extends CMD {

    private String colour;



    public myDsl_PENCOLOUR(
        String colour    ) {
        super(
        );
        this.colour = colour;
    }


    public String getColour() {
        return colour;
    }

    public void setColour(String colour) {
        this.colour = colour;
    }


}