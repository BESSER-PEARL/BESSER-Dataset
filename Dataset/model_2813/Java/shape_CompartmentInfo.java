





import java.util.List;
import java.util.ArrayList;

public class shape_CompartmentInfo  {

    private boolean invisible;
    private int spacing;
    private int margin;
    private String compartmentLayout;
    private String stretchV;
    private String stretchH;





    private shape_TextBody shape_textbody;




    private shape_Rectangle shape_rectangle;




    private shape_Ellipse shape_ellipse;


    public shape_CompartmentInfo(
        boolean invisible,        int spacing,        int margin,        String compartmentLayout,        String stretchV,        String stretchH    ) {
        this.invisible = invisible;
        this.spacing = spacing;
        this.margin = margin;
        this.compartmentLayout = compartmentLayout;
        this.stretchV = stretchV;
        this.stretchH = stretchH;
    }


    public boolean getInvisible() {
        return invisible;
    }

    public void setInvisible(boolean invisible) {
        this.invisible = invisible;
    }
    public int getSpacing() {
        return spacing;
    }

    public void setSpacing(int spacing) {
        this.spacing = spacing;
    }
    public int getMargin() {
        return margin;
    }

    public void setMargin(int margin) {
        this.margin = margin;
    }
    public String getCompartmentlayout() {
        return compartmentLayout;
    }

    public void setCompartmentlayout(String compartmentLayout) {
        this.compartmentLayout = compartmentLayout;
    }
    public String getStretchv() {
        return stretchV;
    }

    public void setStretchv(String stretchV) {
        this.stretchV = stretchV;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }

    public shape_TextBody getShape_textbody() {
        return shape_textbody;
    }

    public void setShape_textbody(shape_TextBody shape_textbody) {
        this.shape_textbody = shape_textbody;
    }
    public shape_Rectangle getShape_rectangle() {
        return shape_rectangle;
    }

    public void setShape_rectangle(shape_Rectangle shape_rectangle) {
        this.shape_rectangle = shape_rectangle;
    }
    public shape_Ellipse getShape_ellipse() {
        return shape_ellipse;
    }

    public void setShape_ellipse(shape_Ellipse shape_ellipse) {
        this.shape_ellipse = shape_ellipse;
    }

}