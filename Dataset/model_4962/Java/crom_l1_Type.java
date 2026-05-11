





import java.util.List;
import java.util.ArrayList;

public class crom_l1_Type extends RelationTarget {






    private crom_l1_Operation crom_l1_operation;




    private List<crom_l1_Operation> crom_l1_operations;




    private crom_l1_Attribute crom_l1_attribute;




    private crom_l1_TypedElement crom_l1_typedelement;




    private List<crom_l1_Attribute> crom_l1_attributes;


    public crom_l1_Type(
    ) {
        super(
        );
        this.crom_l1_operations = new ArrayList<>();
        this.crom_l1_attributes = new ArrayList<>();
    }

    public crom_l1_Type(
        ArrayList<crom_l1_Operation> crom_l1_operations,        ArrayList<crom_l1_Attribute> crom_l1_attributes    ) {
        this.crom_l1_operations = crom_l1_operations;
        this.crom_l1_attributes = crom_l1_attributes;
    }


    public crom_l1_Operation getCrom_l1_operation() {
        return crom_l1_operation;
    }

    public void setCrom_l1_operation(crom_l1_Operation crom_l1_operation) {
        this.crom_l1_operation = crom_l1_operation;
    }
    public List<crom_l1_Operation> getCrom_l1_operations() {
        return crom_l1_operations;
    }

    public void addCrom_l1_operation(Crom_l1_operation crom_l1_operation) {
        this.crom_l1_operations.add(crom_l1_operation);
    }
    public crom_l1_Attribute getCrom_l1_attribute() {
        return crom_l1_attribute;
    }

    public void setCrom_l1_attribute(crom_l1_Attribute crom_l1_attribute) {
        this.crom_l1_attribute = crom_l1_attribute;
    }
    public crom_l1_TypedElement getCrom_l1_typedelement() {
        return crom_l1_typedelement;
    }

    public void setCrom_l1_typedelement(crom_l1_TypedElement crom_l1_typedelement) {
        this.crom_l1_typedelement = crom_l1_typedelement;
    }
    public List<crom_l1_Attribute> getCrom_l1_attributes() {
        return crom_l1_attributes;
    }

    public void addCrom_l1_attribute(Crom_l1_attribute crom_l1_attribute) {
        this.crom_l1_attributes.add(crom_l1_attribute);
    }

}