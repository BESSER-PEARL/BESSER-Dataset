





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Font  {

    private String decoration;
    private String style;
    private float rotation;
    private String size;
    private String align;
    private String weight;
    private String family;





    private pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics;


    public pnmlcoremodel_Font(
        String decoration,        String style,        float rotation,        String size,        String align,        String weight,        String family    ) {
        this.decoration = decoration;
        this.style = style;
        this.rotation = rotation;
        this.size = size;
        this.align = align;
        this.weight = weight;
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
    public float getRotation() {
        return rotation;
    }

    public void setRotation(float rotation) {
        this.rotation = rotation;
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

    public pnmlcoremodel_AnnotationGraphics getPnmlcoremodel_annotationgraphics() {
        return pnmlcoremodel_annotationgraphics;
    }

    public void setPnmlcoremodel_annotationgraphics(pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics) {
        this.pnmlcoremodel_annotationgraphics = pnmlcoremodel_annotationgraphics;
    }

}