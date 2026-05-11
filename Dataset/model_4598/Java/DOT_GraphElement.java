





import java.util.List;
import java.util.ArrayList;

public class DOT_GraphElement  {

    private String style;
    private String color;
    private String name;





    private DOT_Label dot_label;




    private DOT_Label dot_label;


    public DOT_GraphElement(
        String style,        String color,        String name    ) {
        this.style = style;
        this.color = color;
        this.name = name;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DOT_Label getDot_label() {
        return dot_label;
    }

    public void setDot_label(DOT_Label dot_label) {
        this.dot_label = dot_label;
    }
    public DOT_Label getDot_label() {
        return dot_label;
    }

    public void setDot_label(DOT_Label dot_label) {
        this.dot_label = dot_label;
    }

}