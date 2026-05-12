





import java.util.List;
import java.util.ArrayList;

public class HTML_FRAME  {

    private String marginwidth;
    private String scrolling;
    private String src;
    private String noresize;
    private String name;
    private String marginheight;



    public HTML_FRAME(
        String marginwidth,        String scrolling,        String src,        String noresize,        String name,        String marginheight    ) {
        this.marginwidth = marginwidth;
        this.scrolling = scrolling;
        this.src = src;
        this.noresize = noresize;
        this.name = name;
        this.marginheight = marginheight;
    }


    public String getMarginwidth() {
        return marginwidth;
    }

    public void setMarginwidth(String marginwidth) {
        this.marginwidth = marginwidth;
    }
    public String getScrolling() {
        return scrolling;
    }

    public void setScrolling(String scrolling) {
        this.scrolling = scrolling;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMarginheight() {
        return marginheight;
    }

    public void setMarginheight(String marginheight) {
        this.marginheight = marginheight;
    }


}