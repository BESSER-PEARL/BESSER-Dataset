





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String text;
    private String link;
    private String alink;
    private String vlink;
    private String background;
    private String bgcolor;





    private HTML html;


    public HTML_BODY(
        String text,        String link,        String alink,        String vlink,        String background,        String bgcolor    ) {
        super(
        );
        this.text = text;
        this.link = link;
        this.alink = alink;
        this.vlink = vlink;
        this.background = background;
        this.bgcolor = bgcolor;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getAlink() {
        return alink;
    }

    public void setAlink(String alink) {
        this.alink = alink;
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
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }

    public HTML getHtml() {
        return html;
    }

    public void setHtml(HTML html) {
        this.html = html;
    }

}