





import java.util.List;
import java.util.ArrayList;

public class web_Author  {

    private String email;
    private String plusLink;
    private String name;





    private web_Site web_site;


    public web_Author(
        String email,        String plusLink,        String name    ) {
        this.email = email;
        this.plusLink = plusLink;
        this.name = name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPluslink() {
        return plusLink;
    }

    public void setPluslink(String plusLink) {
        this.plusLink = plusLink;
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