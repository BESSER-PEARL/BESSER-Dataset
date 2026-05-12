





import java.util.List;
import java.util.ArrayList;

public class HTML_IMG extends BODYElement {

    private String ismap;
    private String alt;
    private String src;
    private String vspace;
    private String usemap;
    private String width;
    private String hspace;
    private String border;
    private String height;
    private String align;



    public HTML_IMG(
        String ismap,        String alt,        String src,        String vspace,        String usemap,        String width,        String hspace,        String border,        String height,        String align    ) {
        super(
        );
        this.ismap = ismap;
        this.alt = alt;
        this.src = src;
        this.vspace = vspace;
        this.usemap = usemap;
        this.width = width;
        this.hspace = hspace;
        this.border = border;
        this.height = height;
        this.align = align;
    }


    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
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
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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


}