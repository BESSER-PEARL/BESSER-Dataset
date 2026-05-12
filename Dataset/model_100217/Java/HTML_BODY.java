





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String link;
    private String bgcolor;
    private String text;
    private String vlink;
    private String background;
    private String alink;



    public HTML_BODY(
        String link,        String bgcolor,        String text,        String vlink,        String background,        String alink    ) {
        super(
        );
        this.link = link;
        this.bgcolor = bgcolor;
        this.text = text;
        this.vlink = vlink;
        this.background = background;
        this.alink = alink;
    }


    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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
    public String getAlink() {
        return alink;
    }

    public void setAlink(String alink) {
        this.alink = alink;
    }


}