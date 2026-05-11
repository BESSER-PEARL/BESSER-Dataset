





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_SquareDescription extends NodeStyleDescription {

    private String height;
    private String width;





    private ColorDescription colordescription;


    public viewpoint_style_SquareDescription(
        String height,        String width    ) {
        super(
        );
        this.height = height;
        this.width = width;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}