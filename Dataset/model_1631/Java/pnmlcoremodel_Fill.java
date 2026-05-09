





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Fill  {

    private String color;
    private String gradientColor;
    private String gradientrotation;
    private String image;





    private pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics;




    private pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics;


    public pnmlcoremodel_Fill(
        String color,        String gradientColor,        String gradientrotation,        String image    ) {
        this.color = color;
        this.gradientColor = gradientColor;
        this.gradientrotation = gradientrotation;
        this.image = image;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getGradientcolor() {
        return gradientColor;
    }

    public void setGradientcolor(String gradientColor) {
        this.gradientColor = gradientColor;
    }
    public String getGradientrotation() {
        return gradientrotation;
    }

    public void setGradientrotation(String gradientrotation) {
        this.gradientrotation = gradientrotation;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public pnmlcoremodel_AnnotationGraphics getPnmlcoremodel_annotationgraphics() {
        return pnmlcoremodel_annotationgraphics;
    }

    public void setPnmlcoremodel_annotationgraphics(pnmlcoremodel_AnnotationGraphics pnmlcoremodel_annotationgraphics) {
        this.pnmlcoremodel_annotationgraphics = pnmlcoremodel_annotationgraphics;
    }
    public pnmlcoremodel_NodeGraphics getPnmlcoremodel_nodegraphics() {
        return pnmlcoremodel_nodegraphics;
    }

    public void setPnmlcoremodel_nodegraphics(pnmlcoremodel_NodeGraphics pnmlcoremodel_nodegraphics) {
        this.pnmlcoremodel_nodegraphics = pnmlcoremodel_nodegraphics;
    }

}