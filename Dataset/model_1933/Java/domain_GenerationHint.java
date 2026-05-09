





import java.util.List;
import java.util.ArrayList;

public class domain_GenerationHint  {

    private String uid;
    private String name;
    private String applyedClass;





    private domain_Classifier domain_classifier;


    public domain_GenerationHint(
        String uid,        String name,        String applyedClass    ) {
        this.uid = uid;
        this.name = name;
        this.applyedClass = applyedClass;
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
    public String getApplyedclass() {
        return applyedClass;
    }

    public void setApplyedclass(String applyedClass) {
        this.applyedClass = applyedClass;
    }

    public domain_Classifier getDomain_classifier() {
        return domain_classifier;
    }

    public void setDomain_classifier(domain_Classifier domain_classifier) {
        this.domain_classifier = domain_classifier;
    }

}