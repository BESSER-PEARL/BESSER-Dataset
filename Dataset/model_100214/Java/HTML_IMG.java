





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String usemap;
    private String hspace;
    private String vspace;
    private String border;
    private String src;
    private String height;
    private String width;
    private String alt;
    private String align;
    private String ismap;



    public HTML_IMG(
        String usemap,        String hspace,        String vspace,        String border,        String src,        String height,        String width,        String alt,        String align,        String ismap    ) {
        super(
        );
        this.usemap = usemap;
        this.hspace = hspace;
        this.vspace = vspace;
        this.border = border;
        this.src = src;
        this.height = height;
        this.width = width;
        this.alt = alt;
        this.align = align;
        this.ismap = ismap;
    }


    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }


}