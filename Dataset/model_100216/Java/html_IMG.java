





import java.util.List;
import java.util.ArrayList;

public class html_IMG extends BODYElement {

    private String border;
    private String alt;
    private String usemap;
    private String ismap;
    private String height;
    private String align;
    private String hspace;
    private String width;
    private String vspace;
    private String src;



    public html_IMG(
        String border,        String alt,        String usemap,        String ismap,        String height,        String align,        String hspace,        String width,        String vspace,        String src    ) {
        super(
        );
        this.border = border;
        this.alt = alt;
        this.usemap = usemap;
        this.ismap = ismap;
        this.height = height;
        this.align = align;
        this.hspace = hspace;
        this.width = width;
        this.vspace = vspace;
        this.src = src;
    }


    public String getBorder() {
        return border;
    }

    public void setBorder(String border) {
        this.border = border;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getUsemap() {
        return usemap;
    }

    public void setUsemap(String usemap) {
        this.usemap = usemap;
    }
    public String getIsmap() {
        return ismap;
    }

    public void setIsmap(String ismap) {
        this.ismap = ismap;
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


}