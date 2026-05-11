





import java.util.List;
import java.util.ArrayList;

public class HTML_HTMLElement  {






    private HTML_HTML html_html;




    private List<HTML_HTMLElement> html_htmlelements;


    public HTML_HTMLElement(
    ) {
        this.html_htmlelements = new ArrayList<>();
    }

    public HTML_HTMLElement(
        ArrayList<HTML_HTMLElement> html_htmlelements    ) {
        this.html_htmlelements = html_htmlelements;
    }


    public HTML_HTML getHtml_html() {
        return html_html;
    }

    public void setHtml_html(HTML_HTML html_html) {
        this.html_html = html_html;
    }
    public List<HTML_HTMLElement> getHtml_htmlelements() {
        return html_htmlelements;
    }

    public void addHtml_htmlelement(Html_htmlelement html_htmlelement) {
        this.html_htmlelements.add(html_htmlelement);
    }

}