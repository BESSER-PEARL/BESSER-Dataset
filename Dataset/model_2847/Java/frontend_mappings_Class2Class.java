





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Class2Class extends ClassMapping {

    private String cardinality;





    private List<C2CModifier> c2cmodifiers;




    private List<Attribute2Attribute> attribute2attributes;


    public frontend_mappings_Class2Class(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
        this.c2cmodifiers = new ArrayList<>();
        this.attribute2attributes = new ArrayList<>();
    }

    public frontend_mappings_Class2Class(
        String cardinality        ArrayList<C2CModifier> c2cmodifiers,        ArrayList<Attribute2Attribute> attribute2attributes    ) {
        this.cardinality = cardinality;
        this.c2cmodifiers = c2cmodifiers;
        this.attribute2attributes = attribute2attributes;
    }

    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public List<C2CModifier> getC2cmodifiers() {
        return c2cmodifiers;
    }

    public void addC2cmodifier(C2cmodifier c2cmodifier) {
        this.c2cmodifiers.add(c2cmodifier);
    }
    public List<Attribute2Attribute> getAttribute2attributes() {
        return attribute2attributes;
    }

    public void addAttribute2attribute(Attribute2attribute attribute2attribute) {
        this.attribute2attributes.add(attribute2attribute);
    }

}