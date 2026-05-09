





import java.util.List;
import java.util.ArrayList;

public class domain_Assosiation extends RelationShip {

    private String type;





    private domain_Attribute domain_attribute;




    private domain_Attribute domain_attribute;




    private domain_TypePointer domain_typepointer;


    public domain_Assosiation(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public domain_Attribute getDomain_attribute() {
        return domain_attribute;
    }

    public void setDomain_attribute(domain_Attribute domain_attribute) {
        this.domain_attribute = domain_attribute;
    }
    public domain_Attribute getDomain_attribute() {
        return domain_attribute;
    }

    public void setDomain_attribute(domain_Attribute domain_attribute) {
        this.domain_attribute = domain_attribute;
    }
    public domain_TypePointer getDomain_typepointer() {
        return domain_typepointer;
    }

    public void setDomain_typepointer(domain_TypePointer domain_typepointer) {
        this.domain_typepointer = domain_typepointer;
    }

}