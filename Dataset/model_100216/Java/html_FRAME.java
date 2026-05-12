





import java.util.List;
import java.util.ArrayList;

public class html_FRAME  {

    private String src;
    private String name;
    private String marginwidth;
    private String noresize;
    private String marginheight;
    private String scrolling;



    public html_FRAME(
        String src,        String name,        String marginwidth,        String noresize,        String marginheight,        String scrolling    ) {
        this.src = src;
        this.name = name;
        this.marginwidth = marginwidth;
        this.noresize = noresize;
        this.marginheight = marginheight;
        this.scrolling = scrolling;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }
    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }
    public String getMarginheight() {
        return marginheight;
    }

    public void setMarginheight(String marginheight) {
        this.marginheight = marginheight;
    }
    public String getScrolling() {
        return scrolling;
    }

    public void setScrolling(String scrolling) {
        this.scrolling = scrolling;
    }


}