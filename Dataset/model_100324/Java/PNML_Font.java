





import java.util.List;
import java.util.ArrayList;

public class PNML_Font  {

    private String weight;
    private String decoration;
    private String style;
    private String align;
    private String size;
    private String rotation;
    private String family;





    private AnnotationGraphics annotationgraphics;


    public PNML_Font(
        String weight,        String decoration,        String style,        String align,        String size,        String rotation,        String family    ) {
        this.weight = weight;
        this.decoration = decoration;
        this.style = style;
        this.align = align;
        this.size = size;
        this.rotation = rotation;
        this.family = family;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }
    public String getDecoration() {
        return decoration;
    }

    public void setDecoration(String decoration) {
        this.decoration = decoration;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
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

    public AnnotationGraphics getAnnotationgraphics() {
        return annotationgraphics;
    }

    public void setAnnotationgraphics(AnnotationGraphics annotationgraphics) {
        this.annotationgraphics = annotationgraphics;
    }

}