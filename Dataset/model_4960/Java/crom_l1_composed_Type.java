





import java.util.List;
import java.util.ArrayList;

public class crom_l1_composed_Type extends RelationTarget {






    private crom_l1_composed_Attribute crom_l1_composed_attribute;




    private List<crom_l1_composed_Operation> crom_l1_composed_operations;




    private List<crom_l1_composed_Attribute> crom_l1_composed_attributes;




    private crom_l1_composed_Operation crom_l1_composed_operation;


    public crom_l1_composed_Type(
    ) {
        super(
        );
        this.crom_l1_composed_operations = new ArrayList<>();
        this.crom_l1_composed_attributes = new ArrayList<>();
    }

    public crom_l1_composed_Type(
        ArrayList<crom_l1_composed_Operation> crom_l1_composed_operations,        ArrayList<crom_l1_composed_Attribute> crom_l1_composed_attributes    ) {
        this.crom_l1_composed_operations = crom_l1_composed_operations;
        this.crom_l1_composed_attributes = crom_l1_composed_attributes;
    }


    public crom_l1_composed_Attribute getCrom_l1_composed_attribute() {
        return crom_l1_composed_attribute;
    }

    public void setCrom_l1_composed_attribute(crom_l1_composed_Attribute crom_l1_composed_attribute) {
        this.crom_l1_composed_attribute = crom_l1_composed_attribute;
    }
    public List<crom_l1_composed_Operation> getCrom_l1_composed_operations() {
        return crom_l1_composed_operations;
    }

    public void addCrom_l1_composed_operation(Crom_l1_composed_operation crom_l1_composed_operation) {
        this.crom_l1_composed_operations.add(crom_l1_composed_operation);
    }
    public List<crom_l1_composed_Attribute> getCrom_l1_composed_attributes() {
        return crom_l1_composed_attributes;
    }

    public void addCrom_l1_composed_attribute(Crom_l1_composed_attribute crom_l1_composed_attribute) {
        this.crom_l1_composed_attributes.add(crom_l1_composed_attribute);
    }
    public crom_l1_composed_Operation getCrom_l1_composed_operation() {
        return crom_l1_composed_operation;
    }

    public void setCrom_l1_composed_operation(crom_l1_composed_Operation crom_l1_composed_operation) {
        this.crom_l1_composed_operation = crom_l1_composed_operation;
    }

}