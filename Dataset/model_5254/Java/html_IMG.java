





import java.util.List;
import java.util.ArrayList;

public class html_IMG extends BODYElement {

    private String usemap;
    private String height;
    private String align;
    private String border;
    private String vspace;
    private String ismap;
    private String hspace;
    private String width;
    private String alt;
    private String src;



    public html_IMG(
        String usemap,        String height,        String align,        String border,        String vspace,        String ismap,        String hspace,        String width,        String alt,        String src    ) {
        super(
        );
        this.usemap = usemap;
        this.height = height;
        this.align = align;
        this.border = border;
        this.vspace = vspace;
        this.ismap = ismap;
        this.hspace = hspace;
        this.width = width;
        this.alt = alt;
        this.src = src;
    }


    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
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
    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getVspace() {
        return vspace;
    }

    public void setVspace(String vspace) {
        this.vspace = vspace;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
    }
    public String getHspace() {
        return hspace;
    }

    public void setHspace(String hspace) {
        this.hspace = hspace;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}