





import java.util.List;
import java.util.ArrayList;

public class WebApp_Forms extends IdElement, NamedElement {






    private List<WebApp_FormElements> webapp_formelementss;


    public WebApp_Forms(
    ) {
        super(
        );
        this.webapp_formelementss = new ArrayList<>();
    }

    public WebApp_Forms(
        ArrayList<WebApp_FormElements> webapp_formelementss    ) {
        this.webapp_formelementss = webapp_formelementss;
    }


    public List<WebApp_FormElements> getWebapp_formelementss() {
        return webapp_formelementss;
    }

    public void addWebapp_formelements(Webapp_formelements webapp_formelements) {
        this.webapp_formelementss.add(webapp_formelements);
    }

}