





import java.util.List;
import java.util.ArrayList;

public class domain_HashProperty  {

    private String uid;
    private String fakeName;





    private domain_ConfigHash domain_confighash;




    private domain_Configuration domain_configuration;


    public domain_HashProperty(
        String uid,        String fakeName    ) {
        this.uid = uid;
        this.fakeName = fakeName;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getFakename() {
        return fakeName;
    }

    public void setFakename(String fakeName) {
        this.fakeName = fakeName;
    }

    public domain_ConfigHash getDomain_confighash() {
        return domain_confighash;
    }

    public void setDomain_confighash(domain_ConfigHash domain_confighash) {
        this.domain_confighash = domain_confighash;
    }
    public domain_Configuration getDomain_configuration() {
        return domain_configuration;
    }

    public void setDomain_configuration(domain_Configuration domain_configuration) {
        this.domain_configuration = domain_configuration;
    }

}