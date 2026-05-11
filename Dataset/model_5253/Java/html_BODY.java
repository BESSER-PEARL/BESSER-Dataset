





import java.util.List;
import java.util.ArrayList;

public class html_BODY extends HTMLElement {

    private String text;
    private String bgcolor;
    private String alink;
    private String link;
    private String vlink;
    private String background;



    public html_BODY(
        String text,        String bgcolor,        String alink,        String link,        String vlink,        String background    ) {
        super(
        );
        this.text = text;
        this.bgcolor = bgcolor;
        this.alink = alink;
        this.link = link;
        this.vlink = vlink;
        this.background = background;
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
    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
    }


}