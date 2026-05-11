





import java.util.List;
import java.util.ArrayList;

public class html_EMBED extends BODYElement {

    private String vspace;
    private String hspace;
    private String src;
    private String border;
    private String height;
    private String align;
    private String width;



    public html_EMBED(
        String vspace,        String hspace,        String src,        String border,        String height,        String align,        String width    ) {
        super(
        );
        this.vspace = vspace;
        this.hspace = hspace;
        this.src = src;
        this.border = border;
        this.height = height;
        this.align = align;
        this.width = width;
    }


    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}