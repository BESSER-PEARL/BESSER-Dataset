





import java.util.List;
import java.util.ArrayList;

public class crom_l1_Type extends RelationTarget {






    private crom_l1_Attribute crom_l1_attribute;




    private List<crom_l1_Attribute> crom_l1_attributes;


    public crom_l1_Type(
    ) {
        super(
        );
        this.crom_l1_attributes = new ArrayList<>();
    }

    public crom_l1_Type(
        ArrayList<crom_l1_Attribute> crom_l1_attributes    ) {
        this.crom_l1_attributes = crom_l1_attributes;
    }


    public crom_l1_Attribute getCrom_l1_attribute() {
        return crom_l1_attribute;
    }

    public void setCrom_l1_attribute(crom_l1_Attribute crom_l1_attribute) {
        this.crom_l1_attribute = crom_l1_attribute;
    }
    public List<crom_l1_Attribute> getCrom_l1_attributes() {
        return crom_l1_attributes;
    }

    public void addCrom_l1_attribute(Crom_l1_attribute crom_l1_attribute) {
        this.crom_l1_attributes.add(crom_l1_attribute);
    }

}