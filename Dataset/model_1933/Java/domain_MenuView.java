





import java.util.List;
import java.util.ArrayList;

public class domain_MenuView  {

    private String uid;





    private domain_MenuDefinition domain_menudefinition;




    private domain_EObject domain_eobject;




    private List<domain_MenuFolder> domain_menufolders;




    private domain_MenuDefinition domain_menudefinition;


    public domain_MenuView(
        String uid    ) {
        this.uid = uid;
        this.domain_menufolders = new ArrayList<>();
    }

    public domain_MenuView(
        String uid        ArrayList<domain_MenuFolder> domain_menufolders    ) {
        this.uid = uid;
        this.domain_menufolders = domain_menufolders;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_MenuDefinition getDomain_menudefinition() {
        return domain_menudefinition;
    }

    public void setDomain_menudefinition(domain_MenuDefinition domain_menudefinition) {
        this.domain_menudefinition = domain_menudefinition;
    }
    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }
    public List<domain_MenuFolder> getDomain_menufolders() {
        return domain_menufolders;
    }

    public void addDomain_menufolder(Domain_menufolder domain_menufolder) {
        this.domain_menufolders.add(domain_menufolder);
    }
    public domain_MenuDefinition getDomain_menudefinition() {
        return domain_menudefinition;
    }

    public void setDomain_menudefinition(domain_MenuDefinition domain_menudefinition) {
        this.domain_menudefinition = domain_menudefinition;
    }

}