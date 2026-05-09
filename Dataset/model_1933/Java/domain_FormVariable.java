





import java.util.List;
import java.util.ArrayList;

public class domain_FormVariable extends TypePointer {

    private String name;
    private String uid;





    private domain_FormParameter domain_formparameter;


    public domain_FormVariable(
        String name,        String uid    ) {
        super(
        );
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

    public domain_FormParameter getDomain_formparameter() {
        return domain_formparameter;
    }

    public void setDomain_formparameter(domain_FormParameter domain_formparameter) {
        this.domain_formparameter = domain_formparameter;
    }

}