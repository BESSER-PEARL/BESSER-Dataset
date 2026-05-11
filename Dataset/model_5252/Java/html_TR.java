





import java.util.List;
import java.util.ArrayList;

public class html_TR extends TABLEElement {

    private String valign;
    private String align;





    private List<html_TD> html_tds;




    private html_TABLE html_table;




    private html_TABLE html_table;




    private html_TD html_td;


    public html_TR(
        String valign,        String align    ) {
        super(
        );
        this.valign = valign;
        this.align = align;
        this.html_tds = new ArrayList<>();
    }

    public html_TR(
        String valign,        String align        ArrayList<html_TD> html_tds    ) {
        this.valign = valign;
        this.align = align;
        this.html_tds = html_tds;
    }

    public String getValign() {
        return valign;
    }

    public void setValign(String valign) {
        this.valign = valign;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }

    public List<html_TD> getHtml_tds() {
        return html_tds;
    }

    public void addHtml_td(Html_td html_td) {
        this.html_tds.add(html_td);
    }
    public html_TABLE getHtml_table() {
        return html_table;
    }

    public void setHtml_table(html_TABLE html_table) {
        this.html_table = html_table;
    }
    public html_TABLE getHtml_table() {
        return html_table;
    }

    public void setHtml_table(html_TABLE html_table) {
        this.html_table = html_table;
    }
    public html_TD getHtml_td() {
        return html_td;
    }

    public void setHtml_td(html_TD html_td) {
        this.html_td = html_td;
    }

}