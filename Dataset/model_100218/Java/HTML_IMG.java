





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String hspace;
    private String height;
    private String border;
    private String align;
    private String alt;
    private String ismap;
    private String width;
    private String vspace;
    private String usemap;
    private String src;



    public HTML_IMG(
        String hspace,        String height,        String border,        String align,        String alt,        String ismap,        String width,        String vspace,        String usemap,        String src    ) {
        super(
        );
        this.hspace = hspace;
        this.height = height;
        this.border = border;
        this.align = align;
        this.alt = alt;
        this.ismap = ismap;
        this.width = width;
        this.vspace = vspace;
        this.usemap = usemap;
        this.src = src;
    }


    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
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
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}