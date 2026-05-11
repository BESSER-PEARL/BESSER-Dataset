





import java.util.List;
import java.util.ArrayList;

public class ric_ObjectComponent  {

    private int vspace;
    private int height;
    private int border;
    private int hspace;
    private String align;
    private int width;





    private ric_Div ric_div;




    private ric_Document ric_document;


    public ric_ObjectComponent(
        int vspace,        int height,        int border,        int hspace,        String align,        int width    ) {
        this.vspace = vspace;
        this.height = height;
        this.border = border;
        this.hspace = hspace;
        this.align = align;
        this.width = width;
    }


    public int getVspace() {
        return vspace;
    }

    public void setVspace(int vspace) {
        this.vspace = vspace;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getBorder() {
        return border;
    }

    public void setBorder(int border) {
        this.border = border;
    }
    public int getHspace() {
        return hspace;
    }

    public void setHspace(int hspace) {
        this.hspace = hspace;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
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