





import java.util.List;
import java.util.ArrayList;

public class HTML_HTMLElement  {






    private HTML_HTML html_html;




    private List<HTML_Style> html_styles;




    private List<HTML_HTMLElement> html_htmlelements;


    public HTML_HTMLElement(
    ) {
        this.html_styles = new ArrayList<>();
        this.html_htmlelements = new ArrayList<>();
    }

    public HTML_HTMLElement(
        ArrayList<HTML_Style> html_styles,        ArrayList<HTML_HTMLElement> html_htmlelements    ) {
        this.html_styles = html_styles;
        this.html_htmlelements = html_htmlelements;
    }


    public HTML_HTML getHtml_html() {
        return html_html;
    }

    public void setHtml_html(HTML_HTML html_html) {
        this.html_html = html_html;
    }
    public List<HTML_Style> getHtml_styles() {
        return html_styles;
    }

    public void addHtml_style(Html_style html_style) {
        this.html_styles.add(html_style);
    }
    public List<HTML_HTMLElement> getHtml_htmlelements() {
        return html_htmlelements;
    }

    public void addHtml_htmlelement(Html_htmlelement html_htmlelement) {
        this.html_htmlelements.add(html_htmlelement);
    }

}