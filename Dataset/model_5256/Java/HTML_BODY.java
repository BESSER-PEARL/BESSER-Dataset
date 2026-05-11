





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String background;
    private String alink;
    private String link;
    private String vlink;
    private String text;
    private String bgcolor;



    public HTML_BODY(
        String background,        String alink,        String link,        String vlink,        String text,        String bgcolor    ) {
        super(
        );
        this.background = background;
        this.alink = alink;
        this.link = link;
        this.vlink = vlink;
        this.text = text;
        this.bgcolor = bgcolor;
    }


    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
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
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }


}