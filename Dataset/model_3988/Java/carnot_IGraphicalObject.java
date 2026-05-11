





import java.util.List;
import java.util.ArrayList;

public class carnot_IGraphicalObject extends IModelElement {

    private String fillColor;
    private String style;
    private String borderColor;



    public carnot_IGraphicalObject(
        String fillColor,        String style,        String borderColor    ) {
        super(
        );
        this.fillColor = fillColor;
        this.style = style;
        this.borderColor = borderColor;
    }


    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getBordercolor() {
        return borderColor;
    }

    public void setBordercolor(String borderColor) {
        this.borderColor = borderColor;
    }


}