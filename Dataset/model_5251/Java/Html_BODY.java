





import java.util.List;
import java.util.ArrayList;

public class Html_BODY extends HTMLElement {

    private String background;
    private String bgcolor;
    private String vlink;
    private String text;
    private String link;
    private String alink;





    private List<BODYElement> bodyelements;


    public Html_BODY(
        String background,        String bgcolor,        String vlink,        String text,        String link,        String alink    ) {
        super(
        );
        this.background = background;
        this.bgcolor = bgcolor;
        this.vlink = vlink;
        this.text = text;
        this.link = link;
        this.alink = alink;
        this.bodyelements = new ArrayList<>();
    }

    public Html_BODY(
        String background,        String bgcolor,        String vlink,        String text,        String link,        String alink        ArrayList<BODYElement> bodyelements    ) {
        this.background = background;
        this.bgcolor = bgcolor;
        this.vlink = vlink;
        this.text = text;
        this.link = link;
        this.alink = alink;
        this.bodyelements = bodyelements;
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

    public List<BODYElement> getBodyelements() {
        return bodyelements;
    }

    public void addBodyelement(Bodyelement bodyelement) {
        this.bodyelements.add(bodyelement);
    }

}