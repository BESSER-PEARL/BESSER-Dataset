





import java.util.List;
import java.util.ArrayList;

public class HTML_BODY extends HTMLElement {

    private String background;
    private String text;
    private String vlink;
    private String link;
    private String bgcolor;
    private String alink;





    private List<BODYElement> bodyelements;




    private HTML html;


    public HTML_BODY(
        String background,        String text,        String vlink,        String link,        String bgcolor,        String alink    ) {
        super(
        );
        this.background = background;
        this.text = text;
        this.vlink = vlink;
        this.link = link;
        this.bgcolor = bgcolor;
        this.alink = alink;
        this.bodyelements = new ArrayList<>();
    }

    public HTML_BODY(
        String background,        String text,        String vlink,        String link,        String bgcolor,        String alink        ArrayList<BODYElement> bodyelements    ) {
        this.background = background;
        this.text = text;
        this.vlink = vlink;
        this.link = link;
        this.bgcolor = bgcolor;
        this.alink = alink;
        this.bodyelements = bodyelements;
    }

    public String getBackground() {
        return background;
    }

    public void setBackground(String background) {
        this.background = background;
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
    public String getAlink() {
        return alink;
    }

    public void setAlink(String alink) {
        this.alink = alink;
    }

    public List<BODYElement> getBodyelements() {
        return bodyelements;
    }

    public void addBodyelement(Bodyelement bodyelement) {
        this.bodyelements.add(bodyelement);
    }
    public HTML getHtml() {
        return html;
    }

    public void setHtml(HTML html) {
        this.html = html;
    }

}