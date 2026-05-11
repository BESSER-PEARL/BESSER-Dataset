





import java.util.List;
import java.util.ArrayList;

public class eJSL_Author  {

    private String authorurl;
    private String name;
    private String authoremail;





    private eJSL_Manifestation ejsl_manifestation;


    public eJSL_Author(
        String authorurl,        String name,        String authoremail    ) {
        this.authorurl = authorurl;
        this.name = name;
        this.authoremail = authoremail;
    }


    public String getAuthorurl() {
        return authorurl;
    }

    public void setAuthorurl(String authorurl) {
        this.authorurl = authorurl;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAuthoremail() {
        return authoremail;
    }

    public void setAuthoremail(String authoremail) {
        this.authoremail = authoremail;
    }

    public eJSL_Manifestation getEjsl_manifestation() {
        return ejsl_manifestation;
    }

    public void setEjsl_manifestation(eJSL_Manifestation ejsl_manifestation) {
        this.ejsl_manifestation = ejsl_manifestation;
    }

}