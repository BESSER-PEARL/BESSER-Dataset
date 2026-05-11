





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String height;
    private String hspace;
    private String alt;
    private String border;
    private String align;
    private String width;
    private String usemap;
    private String vspace;
    private String src;
    private String ismap;



    public HTML_IMG(
        String height,        String hspace,        String alt,        String border,        String align,        String width,        String usemap,        String vspace,        String src,        String ismap    ) {
        super(
        );
        this.height = height;
        this.hspace = hspace;
        this.alt = alt;
        this.border = border;
        this.align = align;
        this.width = width;
        this.usemap = usemap;
        this.vspace = vspace;
        this.src = src;
        this.ismap = ismap;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
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
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }


}