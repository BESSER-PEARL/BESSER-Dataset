





import java.util.List;
import java.util.ArrayList;

public class web_Author  {

    private String name;
    private String plusLink;
    private String email;





    private web_Site web_site;




    private web_NewsEntry web_newsentry;


    public web_Author(
        String name,        String plusLink,        String email    ) {
        this.name = name;
        this.plusLink = plusLink;
        this.email = email;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPluslink() {
        return plusLink;
    }

    public void setPluslink(String plusLink) {
        this.plusLink = plusLink;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public web_Site getWeb_site() {
        return web_site;
    }

    public void setWeb_site(web_Site web_site) {
        this.web_site = web_site;
    }
    public web_NewsEntry getWeb_newsentry() {
        return web_newsentry;
    }

    public void setWeb_newsentry(web_NewsEntry web_newsentry) {
        this.web_newsentry = web_newsentry;
    }

}