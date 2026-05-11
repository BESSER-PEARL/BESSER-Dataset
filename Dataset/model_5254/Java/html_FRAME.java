





import java.util.List;
import java.util.ArrayList;

public class html_FRAME  {

    private String noresize;
    private String marginwidth;
    private String src;
    private String marginheight;
    private String scrolling;
    private String name;



    public html_FRAME(
        String noresize,        String marginwidth,        String src,        String marginheight,        String scrolling,        String name    ) {
        this.noresize = noresize;
        this.marginwidth = marginwidth;
        this.src = src;
        this.marginheight = marginheight;
        this.scrolling = scrolling;
        this.name = name;
    }


    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }
    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}