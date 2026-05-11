





import java.util.List;
import java.util.ArrayList;

public class yuml_ColorableElement extends ModelElement {

    private String color;



    public yuml_ColorableElement(
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