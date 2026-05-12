





import java.util.List;
import java.util.ArrayList;

public class HTML_HEAD extends HTMLElement {






    private HTML html;




    private List<HEADElement> headelements;


    public HTML_HEAD(
    ) {
        super(
        );
        this.headelements = new ArrayList<>();
    }

    public HTML_HEAD(
        ArrayList<HEADElement> headelements    ) {
        this.headelements = headelements;
    }


    public HTML getHtml() {
        return html;
    }

    public void setHtml(HTML html) {
        this.html = html;
    }
    public List<HEADElement> getHeadelements() {
        return headelements;
    }

    public void addHeadelement(Headelement headelement) {
        this.headelements.add(headelement);
    }

}