





import java.util.List;
import java.util.ArrayList;

public class html_EMBED extends BODYElement {

    private String border;
    private String align;
    private String hspace;
    private String src;
    private String vspace;
    private String width;
    private String height;



    public html_EMBED(
        String border,        String align,        String hspace,        String src,        String vspace,        String width,        String height    ) {
        super(
        );
        this.border = border;
        this.align = align;
        this.hspace = hspace;
        this.src = src;
        this.vspace = vspace;
        this.width = width;
        this.height = height;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}