





import java.util.List;
import java.util.ArrayList;

public class defaultname_EMBED extends BODYElement {

    private String src;
    private String hspace;
    private String border;
    private String align;
    private String height;
    private String vspace;
    private String width;



    public defaultname_EMBED(
        String src,        String hspace,        String border,        String align,        String height,        String vspace,        String width    ) {
        super(
        );
        this.src = src;
        this.hspace = hspace;
        this.border = border;
        this.align = align;
        this.height = height;
        this.vspace = vspace;
        this.width = width;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
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
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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


}