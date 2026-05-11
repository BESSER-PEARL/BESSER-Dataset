





import java.util.List;
import java.util.ArrayList;

public class web_Version  {

    private String name;
    private String state;





    private web_Site web_site;


    public web_Version(
        String name,        String state    ) {
        this.name = name;
        this.state = state;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public web_Site getWeb_site() {
        return web_site;
    }

    public void setWeb_site(web_Site web_site) {
        this.web_site = web_site;
    }

}