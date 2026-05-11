





import java.util.List;
import java.util.ArrayList;

public class tortugaDSL_COLOREABLE extends DRAWING_SENTENCE {

    private String color;



    public tortugaDSL_COLOREABLE(
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