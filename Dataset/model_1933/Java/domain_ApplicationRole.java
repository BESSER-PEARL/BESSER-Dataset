





import java.util.List;
import java.util.ArrayList;

public class domain_ApplicationRole  {

    private String name;
    private String uid;





    private domain_Application domain_application;




    private domain_Application domain_application;


    public domain_ApplicationRole(
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

    public domain_Application getDomain_application() {
        return domain_application;
    }

    public void setDomain_application(domain_Application domain_application) {
        this.domain_application = domain_application;
    }
    public domain_Application getDomain_application() {
        return domain_application;
    }

    public void setDomain_application(domain_Application domain_application) {
        this.domain_application = domain_application;
    }

}