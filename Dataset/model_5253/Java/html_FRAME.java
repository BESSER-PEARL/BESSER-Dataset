





import java.util.List;
import java.util.ArrayList;

public class html_FRAME  {

    private String noresize;
    private String scrolling;
    private String name;
    private String marginwidth;
    private String marginheight;
    private String src;



    public html_FRAME(
        String noresize,        String scrolling,        String name,        String marginwidth,        String marginheight,        String src    ) {
        this.noresize = noresize;
        this.scrolling = scrolling;
        this.name = name;
        this.marginwidth = marginwidth;
        this.marginheight = marginheight;
        this.src = src;
    }


    public String getNoresize() {
        return noresize;
    }

    public void setNoresize(String noresize) {
        this.noresize = noresize;
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
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}