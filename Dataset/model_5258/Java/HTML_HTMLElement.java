





import java.util.List;
import java.util.ArrayList;

public class HTML_HTMLElement  {

    private String value;





    private HTMLElement htmlelement;




    private List<HTMLElement> htmlelements;


    public HTML_HTMLElement(
        String value    ) {
        this.value = value;
        this.htmlelements = new ArrayList<>();
    }

    public HTML_HTMLElement(
        String value        ArrayList<HTMLElement> htmlelements    ) {
        this.value = value;
        this.htmlelements = htmlelements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public HTMLElement getHtmlelement() {
        return htmlelement;
    }

    public void setHtmlelement(HTMLElement htmlelement) {
        this.htmlelement = htmlelement;
    }
    public List<HTMLElement> getHtmlelements() {
        return htmlelements;
    }

    public void addHtmlelement(Htmlelement htmlelement) {
        this.htmlelements.add(htmlelement);
    }

}