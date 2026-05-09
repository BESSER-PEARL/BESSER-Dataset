





import java.util.List;
import java.util.ArrayList;

public class domain_TypeDefinition  {

    private String uid;





    private domain_EObject domain_eobject;




    private List<domain_RelationShip> domain_relationships;


    public domain_TypeDefinition(
        String uid    ) {
        this.uid = uid;
        this.domain_relationships = new ArrayList<>();
    }

    public domain_TypeDefinition(
        String uid        ArrayList<domain_RelationShip> domain_relationships    ) {
        this.uid = uid;
        this.domain_relationships = domain_relationships;
    }

    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_EObject getDomain_eobject() {
        return domain_eobject;
    }

    public void setDomain_eobject(domain_EObject domain_eobject) {
        this.domain_eobject = domain_eobject;
    }
    public List<domain_RelationShip> getDomain_relationships() {
        return domain_relationships;
    }

    public void addDomain_relationship(Domain_relationship domain_relationship) {
        this.domain_relationships.add(domain_relationship);
    }

}