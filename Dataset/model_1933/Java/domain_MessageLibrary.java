





import java.util.List;
import java.util.ArrayList;

public class domain_MessageLibrary extends Categorized {

    private String uid;
    private String name;





    private domain_Messages domain_messages;


    public domain_MessageLibrary(
        String uid,        String name    ) {
        super(
        );
        this.uid = uid;
        this.name = name;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domain_Messages getDomain_messages() {
        return domain_messages;
    }

    public void setDomain_messages(domain_Messages domain_messages) {
        this.domain_messages = domain_messages;
    }

}