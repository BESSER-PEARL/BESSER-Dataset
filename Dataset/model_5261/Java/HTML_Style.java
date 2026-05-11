





import java.util.List;
import java.util.ArrayList;

public class HTML_Style  {

    private String key;
    private String value;





    private HTML_HTMLElement html_htmlelement;


    public HTML_Style(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public HTML_HTMLElement getHtml_htmlelement() {
        return html_htmlelement;
    }

    public void setHtml_htmlelement(HTML_HTMLElement html_htmlelement) {
        this.html_htmlelement = html_htmlelement;
    }

}