





import java.util.List;
import java.util.ArrayList;

public class domain_Views  {

    private String uid;





    private domain_FormView domain_formview;




    private List<domain_MenuDefinition> domain_menudefinitions;




    private domain_EObject domain_eobject;




    private domain_FormView domain_formview;


    public domain_Views(
        String uid    ) {
        this.uid = uid;
        this.domain_menudefinitions = new ArrayList<>();
    }

    public domain_Views(
        String uid        ArrayList<domain_MenuDefinition> domain_menudefinitions    ) {
        this.uid = uid;
        this.domain_menudefinitions = domain_menudefinitions;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_FormView getDomain_formview() {
        return domain_formview;
    }

    public void setDomain_formview(domain_FormView domain_formview) {
        this.domain_formview = domain_formview;
    }
    public List<domain_MenuDefinition> getDomain_menudefinitions() {
        return domain_menudefinitions;
    }

    public void addDomain_menudefinition(Domain_menudefinition domain_menudefinition) {
        this.domain_menudefinitions.add(domain_menudefinition);
    }
    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }
    public domain_FormView getDomain_formview() {
        return domain_formview;
    }

    public void setDomain_formview(domain_FormView domain_formview) {
        this.domain_formview = domain_formview;
    }

}