





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Font  {

    private float rotation;
    private String family;
    private String decoration;
    private String style;
    private String weight;
    private String align;
    private String size;





    private pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics;


    public pnmlcoremodel_Font(
        float rotation,        String family,        String decoration,        String style,        String weight,        String align,        String size    ) {
        this.rotation = rotation;
        this.family = family;
        this.decoration = decoration;
        this.style = style;
        this.weight = weight;
        this.align = align;
        this.size = size;
    }


    public float getRotation() {
        return rotation;
    }

    public void setRotation(float rotation) {
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
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

    public pnmlcoremodel_AnnotationGraphics getPnmlcoremodel_annotationgraphics() {
        return pnmlcoremodel_annotationgraphics;
    }

    public void setPnmlcoremodel_annotationgraphics(pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics) {
        this.pnmlcoremodel_annotationgraphics = pnmlcoremodel_annotationgraphics;
    }

}