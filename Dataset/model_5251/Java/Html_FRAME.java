





import java.util.List;
import java.util.ArrayList;

public class Html_FRAME  {

    private String scrolling;
    private String marginwidth;
    private String marginheight;
    private String noresize;
    private String src;
    private String name;



    public Html_FRAME(
        String scrolling,        String marginwidth,        String marginheight,        String noresize,        String src,        String name    ) {
        this.scrolling = scrolling;
        this.marginwidth = marginwidth;
        this.marginheight = marginheight;
        this.noresize = noresize;
        this.src = src;
        this.name = name;
    }


    public String getScrolling() {
        return scrolling;
    }

    public void setScrolling(String scrolling) {
        this.scrolling = scrolling;
    }
    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }
    public String getMarginheight() {
        return marginheight;
    }

    public void setMarginheight(String marginheight) {
        this.marginheight = marginheight;
    }
    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
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


}