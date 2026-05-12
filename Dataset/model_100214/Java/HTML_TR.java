





import java.util.List;
import java.util.ArrayList;

public class HTML_TR extends TABLEElement {

    private String align;
    private String valign;





    private List<HTML_TD> html_tds;




    private HTML_TABLE html_table;




    private HTML_TABLE html_table;




    private HTML_TD html_td;


    public HTML_TR(
        String align,        String valign    ) {
        super(
        );
        this.align = align;
        this.valign = valign;
        this.html_tds = new ArrayList<>();
    }

    public HTML_TR(
        String align,        String valign        ArrayList<HTML_TD> html_tds    ) {
        this.align = align;
        this.valign = valign;
        this.html_tds = html_tds;
    }

    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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
    public HTML_TABLE getHtml_table() {
        return html_table;
    }

    public void setHtml_table(HTML_TABLE html_table) {
        this.html_table = html_table;
    }
    public HTML_TD getHtml_td() {
        return html_td;
    }

    public void setHtml_td(HTML_TD html_td) {
        this.html_td = html_td;
    }

}