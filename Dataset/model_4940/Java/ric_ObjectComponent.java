





import java.util.List;
import java.util.ArrayList;

public class ric_ObjectComponent  {

    private int hspace;
    private int border;
    private int width;
    private int height;
    private String align;
    private int vspace;





    private ric_Document ric_document;




    private ric_Div ric_div;


    public ric_ObjectComponent(
        int hspace,        int border,        int width,        int height,        String align,        int vspace    ) {
        this.hspace = hspace;
        this.border = border;
        this.width = width;
        this.height = height;
        this.align = align;
        this.vspace = vspace;
    }


    public int getHspace() {
        return hspace;
    }

    public void setHspace(int hspace) {
        this.hspace = hspace;
    }
    public int getBorder() {
        return border;
    }

    public void setBorder(int border) {
        this.border = border;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public int getVspace() {
        return vspace;
    }

    public void setVspace(int vspace) {
        this.vspace = vspace;
    }

    public ric_Document getRic_document() {
        return ric_document;
    }

    public void setRic_document(ric_Document ric_document) {
        this.ric_document = ric_document;
    }
    public ric_Div getRic_div() {
        return ric_div;
    }

    public void setRic_div(ric_Div ric_div) {
        this.ric_div = ric_div;
    }

}