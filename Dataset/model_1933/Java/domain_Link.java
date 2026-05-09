





import java.util.List;
import java.util.ArrayList;

public class domain_Link  {

    private String uid;





    private domain_Attribute domain_attribute;




    private domain_Assosiation domain_assosiation;




    private domain_Attribute domain_attribute;


    public domain_Link(
        String uid    ) {
        this.uid = uid;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public domain_Attribute getDomain_attribute() {
        return domain_attribute;
    }

    public void setDomain_attribute(domain_Attribute domain_attribute) {
        this.domain_attribute = domain_attribute;
    }
    public domain_Assosiation getDomain_assosiation() {
        return domain_assosiation;
    }

    public void setDomain_assosiation(domain_Assosiation domain_assosiation) {
        this.domain_assosiation = domain_assosiation;
    }
    public domain_Attribute getDomain_attribute() {
        return domain_attribute;
    }

    public void setDomain_attribute(domain_Attribute domain_attribute) {
        this.domain_attribute = domain_attribute;
    }

}