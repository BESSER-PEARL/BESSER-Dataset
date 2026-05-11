





import java.util.List;
import java.util.ArrayList;

public class html_BODY extends HTMLElement {

    private String bgcolor;
    private String background;
    private String link;
    private String vlink;
    private String alink;
    private String text;



    public html_BODY(
        String bgcolor,        String background,        String link,        String vlink,        String alink,        String text    ) {
        super(
        );
        this.bgcolor = bgcolor;
        this.background = background;
        this.link = link;
        this.vlink = vlink;
        this.alink = alink;
        this.text = text;
    }


    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
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
    public String getVlink() {
        return vlink;
    }

    public void setVlink(String vlink) {
        this.vlink = vlink;
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


}