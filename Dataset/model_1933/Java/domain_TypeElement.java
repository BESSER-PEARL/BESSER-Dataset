





import java.util.List;
import java.util.ArrayList;

public class domain_TypeElement  {

    private String uid;
    private String name;





    private domain_TypeDefinition domain_typedefinition;




    private domain_TypePointer domain_typepointer;




    private domain_RelationShip domain_relationship;




    private domain_RelationShip domain_relationship;




    private domain_TypeDefinition domain_typedefinition;


    public domain_TypeElement(
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

    public domain_TypeDefinition getDomain_typedefinition() {
        return domain_typedefinition;
    }

    public void setDomain_typedefinition(domain_TypeDefinition domain_typedefinition) {
        this.domain_typedefinition = domain_typedefinition;
    }
    public domain_TypePointer getDomain_typepointer() {
        return domain_typepointer;
    }

    public void setDomain_typepointer(domain_TypePointer domain_typepointer) {
        this.domain_typepointer = domain_typepointer;
    }
    public domain_RelationShip getDomain_relationship() {
        return domain_relationship;
    }

    public void setDomain_relationship(domain_RelationShip domain_relationship) {
        this.domain_relationship = domain_relationship;
    }
    public domain_RelationShip getDomain_relationship() {
        return domain_relationship;
    }

    public void setDomain_relationship(domain_RelationShip domain_relationship) {
        this.domain_relationship = domain_relationship;
    }
    public domain_TypeDefinition getDomain_typedefinition() {
        return domain_typedefinition;
    }

    public void setDomain_typedefinition(domain_TypeDefinition domain_typedefinition) {
        this.domain_typedefinition = domain_typedefinition;
    }

}