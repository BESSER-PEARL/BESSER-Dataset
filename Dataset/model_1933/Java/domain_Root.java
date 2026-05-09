





import java.util.List;
import java.util.ArrayList;

public class domain_Root  {

    private String uid;
    private String name;





    private domain_Controls domain_controls;




    private List<domain_FormVariable> domain_formvariables;




    private domain_PREFormTrigger domain_preformtrigger;


    public domain_Root(
        String uid,        String name    ) {
        this.uid = uid;
        this.name = name;
        this.domain_formvariables = new ArrayList<>();
    }

    public domain_Root(
        String uid,        String name        ArrayList<domain_FormVariable> domain_formvariables    ) {
        this.uid = uid;
        this.name = name;
        this.domain_formvariables = domain_formvariables;
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

    public domain_Controls getDomain_controls() {
        return domain_controls;
    }

    public void setDomain_controls(domain_Controls domain_controls) {
        this.domain_controls = domain_controls;
    }
    public List<domain_FormVariable> getDomain_formvariables() {
        return domain_formvariables;
    }

    public void addDomain_formvariable(Domain_formvariable domain_formvariable) {
        this.domain_formvariables.add(domain_formvariable);
    }
    public domain_PREFormTrigger getDomain_preformtrigger() {
        return domain_preformtrigger;
    }

    public void setDomain_preformtrigger(domain_PREFormTrigger domain_preformtrigger) {
        this.domain_preformtrigger = domain_preformtrigger;
    }

}