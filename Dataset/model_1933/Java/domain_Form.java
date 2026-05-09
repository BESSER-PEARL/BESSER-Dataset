





import java.util.List;
import java.util.ArrayList;

public class domain_Form  {

    private String name;
    private String uid;





    private List<domain_FormParameter> domain_formparameters;




    private domain_UIPackage domain_uipackage;


    public domain_Form(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
        this.domain_formparameters = new ArrayList<>();
    }

    public domain_Form(
        String name,        String uid        ArrayList<domain_FormParameter> domain_formparameters    ) {
        this.name = name;
        this.uid = uid;
        this.domain_formparameters = domain_formparameters;
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

    public List<domain_FormParameter> getDomain_formparameters() {
        return domain_formparameters;
    }

    public void addDomain_formparameter(Domain_formparameter domain_formparameter) {
        this.domain_formparameters.add(domain_formparameter);
    }
    public domain_UIPackage getDomain_uipackage() {
        return domain_uipackage;
    }

    public void setDomain_uipackage(domain_UIPackage domain_uipackage) {
        this.domain_uipackage = domain_uipackage;
    }

}