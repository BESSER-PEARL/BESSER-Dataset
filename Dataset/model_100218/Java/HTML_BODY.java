





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String vlink;
    private String bgcolor;
    private String alink;
    private String link;
    private String text;
    private String background;



    public HTML_BODY(
        String vlink,        String bgcolor,        String alink,        String link,        String text,        String background    ) {
        super(
        );
        this.vlink = vlink;
        this.bgcolor = bgcolor;
        this.alink = alink;
        this.link = link;
        this.text = text;
        this.background = background;
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
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
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