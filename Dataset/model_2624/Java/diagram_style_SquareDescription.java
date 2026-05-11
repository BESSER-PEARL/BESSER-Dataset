





import java.util.List;
import java.util.ArrayList;

public class diagram_style_SquareDescription extends NodeStyleDescription {

    private String width;
    private String height;





    private ColorDescription colordescription;


    public diagram_style_SquareDescription(
        String width,        String height    ) {
        super(
        );
        this.width = width;
        this.height = height;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}