





import java.util.List;
import java.util.ArrayList;

public class ptnet_Font  {

    private String weight;
    private String rotation;
    private String family;
    private String decoration;
    private String size;
    private String style;
    private String align;



    public ptnet_Font(
        String weight,        String rotation,        String family,        String decoration,        String size,        String style,        String align    ) {
        this.weight = weight;
        this.rotation = rotation;
        this.family = family;
        this.decoration = decoration;
        this.size = size;
        this.style = style;
        this.align = align;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
    public String getDecoration() {
        return decoration;
    }

    public void setDecoration(String decoration) {
        this.decoration = decoration;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }


}