





import java.util.List;
import java.util.ArrayList;

public class web_Link  {

    private String label;
    private String target;





    private web_Site web_site;


    public web_Link(
        String label,        String target    ) {
        this.label = label;
        this.target = target;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    public web_Site getWeb_site() {
        return web_site;
    }

    public void setWeb_site(web_Site web_site) {
        this.web_site = web_site;
    }

}