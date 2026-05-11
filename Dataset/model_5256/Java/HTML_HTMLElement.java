





import java.util.List;
import java.util.ArrayList;

public class HTML_HTMLElement  {

    private String value;





    private List<HTML_HTMLElement> html_htmlelements;


    public HTML_HTMLElement(
        String value    ) {
        this.value = value;
        this.html_htmlelements = new ArrayList<>();
    }

    public HTML_HTMLElement(
        String value        ArrayList<HTML_HTMLElement> html_htmlelements    ) {
        this.value = value;
        this.html_htmlelements = html_htmlelements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<HTML_HTMLElement> getHtml_htmlelements() {
        return html_htmlelements;
    }

    public void addHtml_htmlelement(Html_htmlelement html_htmlelement) {
        this.html_htmlelements.add(html_htmlelement);
    }

}