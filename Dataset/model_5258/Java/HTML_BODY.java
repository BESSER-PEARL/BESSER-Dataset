





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String alink;
    private String text;
    private String bgcolor;
    private String vlink;
    private String background;
    private String link;



    public HTML_BODY(
        String alink,        String text,        String bgcolor,        String vlink,        String background,        String link    ) {
        super(
        );
        this.alink = alink;
        this.text = text;
        this.bgcolor = bgcolor;
        this.vlink = vlink;
        this.background = background;
        this.link = link;
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
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getVlink() {
        return vlink;
    }

    public void setVlink(String vlink) {
        this.vlink = vlink;
    }
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }


}