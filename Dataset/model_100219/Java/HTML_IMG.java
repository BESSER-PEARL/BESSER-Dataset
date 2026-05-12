





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String align;
    private String height;
    private String alt;
    private String ismap;
    private String width;
    private String usemap;
    private String hspace;
    private String vspace;
    private String border;
    private String src;



    public HTML_IMG(
        String align,        String height,        String alt,        String ismap,        String width,        String usemap,        String hspace,        String vspace,        String border,        String src    ) {
        super(
        );
        this.align = align;
        this.height = height;
        this.alt = alt;
        this.ismap = ismap;
        this.width = width;
        this.usemap = usemap;
        this.hspace = hspace;
        this.vspace = vspace;
        this.border = border;
        this.src = src;
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


}