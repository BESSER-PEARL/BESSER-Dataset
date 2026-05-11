





import java.util.List;
import java.util.ArrayList;

public class ric_ObjectComponent  {

    private int border;
    private int vspace;
    private int hspace;
    private int width;
    private String align;
    private int height;





    private ric_Div ric_div;




    private ric_Document ric_document;


    public ric_ObjectComponent(
        int border,        int vspace,        int hspace,        int width,        String align,        int height    ) {
        this.border = border;
        this.vspace = vspace;
        this.hspace = hspace;
        this.width = width;
        this.align = align;
        this.height = height;
    }


    public int getBorder() {
        return border;
    }

    public void setBorder(int border) {
        this.border = border;
    }
    public int getVspace() {
        return vspace;
    }

    public void setVspace(int vspace) {
        this.vspace = vspace;
    }
    public int getHspace() {
        return hspace;
    }

    public void setHspace(int hspace) {
        this.hspace = hspace;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public ric_Div getRic_div() {
        return ric_div;
    }

    public void setRic_div(ric_Div ric_div) {
        this.ric_div = ric_div;
    }
    public ric_Document getRic_document() {
        return ric_document;
    }

    public void setRic_document(ric_Document ric_document) {
        this.ric_document = ric_document;
    }

}