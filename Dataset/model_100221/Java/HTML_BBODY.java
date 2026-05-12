





import java.util.List;
import java.util.ArrayList;

public class HTML_BBODY extends HTMLElement {

    private String vlink;
    private String text;
    private String alink;
    private String link;
    private String background;
    private String bgcolor;



    public HTML_BBODY(
        String vlink,        String text,        String alink,        String link,        String background,        String bgcolor    ) {
        super(
        );
        this.vlink = vlink;
        this.text = text;
        this.alink = alink;
        this.link = link;
        this.background = background;
        this.bgcolor = bgcolor;
    }


    public String getVlink() {
        return vlink;
    }

    public void setVlink(String vlink) {
        this.vlink = vlink;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getAlink() {
        return alink;
    }

    public void setAlink(String alink) {
        this.alink = alink;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }


}