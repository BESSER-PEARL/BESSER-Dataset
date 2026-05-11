





import java.util.List;
import java.util.ArrayList;

public class HTML_TR extends HTMLElement {

    private String height;
    private String align;
    private String bgcolor;
    private String valign;





    private List<HTML_TD> html_tds;




    private HTML_TABLE html_table;


    public HTML_TR(
        String height,        String align,        String bgcolor,        String valign    ) {
        super(
        );
        this.height = height;
        this.align = align;
        this.bgcolor = bgcolor;
        this.valign = valign;
        this.html_tds = new ArrayList<>();
    }

    public HTML_TR(
        String height,        String align,        String bgcolor,        String valign        ArrayList<HTML_TD> html_tds    ) {
        this.height = height;
        this.align = align;
        this.bgcolor = bgcolor;
        this.valign = valign;
        this.html_tds = html_tds;
    }

    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getBgcolor() {
        return bgcolor;
    }

    public void setBgcolor(String bgcolor) {
        this.bgcolor = bgcolor;
    }
    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }

    public List<HTML_TD> getHtml_tds() {
        return html_tds;
    }

    public void addHtml_td(Html_td html_td) {
        this.html_tds.add(html_td);
    }
    public HTML_TABLE getHtml_table() {
        return html_table;
    }

    public void setHtml_table(HTML_TABLE html_table) {
        this.html_table = html_table;
    }

}