





import java.util.List;
import java.util.ArrayList;

public class PNML_Font  {

    private String decoration;
    private String family;
    private String size;
    private String align;
    private String rotation;
    private String weight;
    private String style;



    public PNML_Font(
        String decoration,        String family,        String size,        String align,        String rotation,        String weight,        String style    ) {
        this.decoration = decoration;
        this.family = family;
        this.size = size;
        this.align = align;
        this.rotation = rotation;
        this.weight = weight;
        this.style = style;
    }


    public String getDecoration() {
        return decoration;
    }

    public void setDecoration(String decoration) {
        this.decoration = decoration;
    }
    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}