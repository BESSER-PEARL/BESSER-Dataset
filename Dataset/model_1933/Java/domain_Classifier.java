





import java.util.List;
import java.util.ArrayList;

public class domain_Classifier  {

    private String uid;
    private String details;





    private domain_Categorized domain_categorized;


    public domain_Classifier(
        String uid,        String details    ) {
        this.uid = uid;
        this.details = details;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }

    public domain_Categorized getDomain_categorized() {
        return domain_categorized;
    }

    public void setDomain_categorized(domain_Categorized domain_categorized) {
        this.domain_categorized = domain_categorized;
    }

}