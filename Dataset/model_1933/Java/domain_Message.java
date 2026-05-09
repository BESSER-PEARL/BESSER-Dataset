





import java.util.List;
import java.util.ArrayList;

public class domain_Message  {

    private String name;
    private String uid;





    private domain_MessageLibrary domain_messagelibrary;


    public domain_Message(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

}