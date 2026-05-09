





import java.util.List;
import java.util.ArrayList;

public class domain_FormDataControls  {

    private String uid;
    private String name;





    private domain_Form domain_form;


    public domain_FormDataControls(
        String uid,        String name    ) {
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

    public domain_Form getDomain_form() {
        return domain_form;
    }

    public void setDomain_form(domain_Form domain_form) {
        this.domain_form = domain_form;
    }

}