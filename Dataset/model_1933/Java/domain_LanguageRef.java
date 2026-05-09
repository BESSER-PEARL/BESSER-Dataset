





import java.util.List;
import java.util.ArrayList;

public class domain_LanguageRef  {

    private String uid;





    private domain_MessageLibrary domain_messagelibrary;




    private domain_Language domain_language;


    public domain_LanguageRef(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_MessageLibrary getDomain_messagelibrary() {
        return domain_messagelibrary;
    }

    public void setDomain_messagelibrary(domain_MessageLibrary domain_messagelibrary) {
        this.domain_messagelibrary = domain_messagelibrary;
    }
    public domain_Language getDomain_language() {
        return domain_language;
    }

    public void setDomain_language(domain_Language domain_language) {
        this.domain_language = domain_language;
    }

}