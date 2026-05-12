





import java.util.List;
import java.util.ArrayList;

public class PNML_Font  {

    private String size;
    private String style;
    private String decoration;
    private String align;
    private String weight;
    private String family;
    private String rotation;





    private AnnotationGraphics annotationgraphics;


    public PNML_Font(
        String size,        String style,        String decoration,        String align,        String weight,        String family,        String rotation    ) {
        this.size = size;
        this.style = style;
        this.decoration = decoration;
        this.align = align;
        this.weight = weight;
        this.family = family;
        this.rotation = rotation;
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
    public String getDecoration() {
        return decoration;
    }

    public void setDecoration(String decoration) {
        this.decoration = decoration;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getFamily() {
        return family;
    }

    public void setFamily(String family) {
        this.family = family;
    }
    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }

    public AnnotationGraphics getAnnotationgraphics() {
        return annotationgraphics;
    }

    public void setAnnotationgraphics(AnnotationGraphics annotationgraphics) {
        this.annotationgraphics = annotationgraphics;
    }

}