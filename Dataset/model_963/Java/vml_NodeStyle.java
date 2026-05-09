





import java.util.List;
import java.util.ArrayList;

public class vml_NodeStyle extends GraphStyle {

    private int padding;
    private int borderWidth;



    public vml_NodeStyle(
        int padding,        int borderWidth    ) {
        super(
        );
        this.padding = padding;
        this.borderWidth = borderWidth;
    }


    public int getPadding() {
        return padding;
    }

    public void setPadding(int padding) {
        this.padding = padding;
    }
    public int getBorderwidth() {
        return borderWidth;
    }

    public void setBorderwidth(int borderWidth) {
        this.borderWidth = borderWidth;
    }


}