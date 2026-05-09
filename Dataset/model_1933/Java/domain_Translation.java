





import java.util.List;
import java.util.ArrayList;

public class domain_Translation  {

    private String translation;
    private String uid;





    private domain_LanguageRef domain_languageref;




    private domain_Message domain_message;


    public domain_Translation(
        String translation,        String uid    ) {
        this.translation = translation;
        this.uid = uid;
    }


    public String getTranslation() {
        return translation;
    }

    public void setTranslation(String translation) {
        this.translation = translation;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_LanguageRef getDomain_languageref() {
        return domain_languageref;
    }

    public void setDomain_languageref(domain_LanguageRef domain_languageref) {
        this.domain_languageref = domain_languageref;
    }
    public domain_Message getDomain_message() {
        return domain_message;
    }

    public void setDomain_message(domain_Message domain_message) {
        this.domain_message = domain_message;
    }

}