





import java.util.List;
import java.util.ArrayList;

public class domain_Type extends Categorized, TypeElement {






    private domain_Attribute domain_attribute;




    private domain_Operation domain_operation;




    private List<domain_Attribute> domain_attributes;




    private List<domain_Operation> domain_operations;


    public domain_Type(
    ) {
        super(
        );
        this.domain_attributes = new ArrayList<>();
        this.domain_operations = new ArrayList<>();
    }

    public domain_Type(
        ArrayList<domain_Attribute> domain_attributes,        ArrayList<domain_Operation> domain_operations    ) {
        this.domain_attributes = domain_attributes;
        this.domain_operations = domain_operations;
    }


    public domain_Attribute getDomain_attribute() {
        return domain_attribute;
    }

    public void setDomain_attribute(domain_Attribute domain_attribute) {
        this.domain_attribute = domain_attribute;
    }
    public domain_Operation getDomain_operation() {
        return domain_operation;
    }

    public void setDomain_operation(domain_Operation domain_operation) {
        this.domain_operation = domain_operation;
    }
    public List<domain_Attribute> getDomain_attributes() {
        return domain_attributes;
    }

    public void addDomain_attribute(Domain_attribute domain_attribute) {
        this.domain_attributes.add(domain_attribute);
    }
    public List<domain_Operation> getDomain_operations() {
        return domain_operations;
    }

    public void addDomain_operation(Domain_operation domain_operation) {
        this.domain_operations.add(domain_operation);
    }

}