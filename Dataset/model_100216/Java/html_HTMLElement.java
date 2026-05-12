





import java.util.List;
import java.util.ArrayList;

public class html_HTMLElement  {

    private String value;





    private List<html_HTMLElement> html_htmlelements;




    private html_HTMLElement html_htmlelement;


    public html_HTMLElement(
        String value    ) {
        this.value = value;
        this.html_htmlelements = new ArrayList<>();
    }

    public html_HTMLElement(
        String value        ArrayList<html_HTMLElement> html_htmlelements    ) {
        this.value = value;
        this.html_htmlelements = html_htmlelements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<html_HTMLElement> getHtml_htmlelements() {
        return html_htmlelements;
    }

    public void addHtml_htmlelement(Html_htmlelement html_htmlelement) {
        this.html_htmlelements.add(html_htmlelement);
    }
    public html_HTMLElement getHtml_htmlelement() {
        return html_htmlelement;
    }

    public void setHtml_htmlelement(html_HTMLElement html_htmlelement) {
        this.html_htmlelement = html_htmlelement;
    }

}