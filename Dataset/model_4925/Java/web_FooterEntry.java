





import java.util.List;
import java.util.ArrayList;

public class web_FooterEntry  {

    private String link;
    private String name;





    private web_Site web_site;


    public web_FooterEntry(
        String link,        String name    ) {
        this.link = link;
        this.name = name;
    }


    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public web_Site getWeb_site() {
        return web_site;
    }

    public void setWeb_site(web_Site web_site) {
        this.web_site = web_site;
    }

}