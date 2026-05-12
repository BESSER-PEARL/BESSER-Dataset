





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAME  {

    private String name;
    private String src;
    private String scrolling;
    private String noresize;
    private String marginwidth;
    private String marginheight;



    public HTML_FRAME(
        String name,        String src,        String scrolling,        String noresize,        String marginwidth,        String marginheight    ) {
        this.name = name;
        this.src = src;
        this.scrolling = scrolling;
        this.noresize = noresize;
        this.marginwidth = marginwidth;
        this.marginheight = marginheight;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getScrolling() {
        return scrolling;
    }

    public void setScrolling(String scrolling) {
        this.scrolling = scrolling;
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
    public String getMarginheight() {
        return marginheight;
    }

    public void setMarginheight(String marginheight) {
        this.marginheight = marginheight;
    }


}