





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String link;
    private String vlink;
    private String bgcolor;
    private String alink;
    private String text;
    private String background;



    public HTML_BODY(
        String link,        String vlink,        String bgcolor,        String alink,        String text,        String background    ) {
        super(
        );
        this.link = link;
        this.vlink = vlink;
        this.bgcolor = bgcolor;
        this.alink = alink;
        this.text = text;
        this.background = background;
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
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getAlink() {
        return alink;
    }

    public void setAlink(String alink) {
        this.alink = alink;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }


}