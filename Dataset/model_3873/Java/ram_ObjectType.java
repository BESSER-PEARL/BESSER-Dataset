





import java.util.List;
import java.util.ArrayList;

public class ram_ObjectType extends MappableElement, Type {






    private ram_Attribute ram_attribute;




    private ram_Reference ram_reference;


    public ram_ObjectType(
    ) {
        super(
        );
    }



    public ram_Attribute getRam_attribute() {
        return ram_attribute;
    }

    public void setRam_attribute(ram_Attribute ram_attribute) {
        this.ram_attribute = ram_attribute;
    }
    public ram_Reference getRam_reference() {
        return ram_reference;
    }

    public void setRam_reference(ram_Reference ram_reference) {
        this.ram_reference = ram_reference;
    }

}