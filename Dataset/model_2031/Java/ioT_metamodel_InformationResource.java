





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_InformationResource  {






    private List<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings;




    private List<ioT_metamodel_Attribute> iot_metamodel_attributes;




    private ioT_metamodel_VirtualThing iot_metamodel_virtualthing;


    public ioT_metamodel_InformationResource(
    ) {
        this.iot_metamodel_physicalthings = new ArrayList<>();
        this.iot_metamodel_attributes = new ArrayList<>();
    }

    public ioT_metamodel_InformationResource(
        ArrayList<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings,        ArrayList<ioT_metamodel_Attribute> iot_metamodel_attributes    ) {
        this.iot_metamodel_physicalthings = iot_metamodel_physicalthings;
        this.iot_metamodel_attributes = iot_metamodel_attributes;
    }


    public List<ioT_metamodel_PhysicalThing> getIot_metamodel_physicalthings() {
        return iot_metamodel_physicalthings;
    }

    public void addIot_metamodel_physicalthing(Iot_metamodel_physicalthing iot_metamodel_physicalthing) {
        this.iot_metamodel_physicalthings.add(iot_metamodel_physicalthing);
    }
    public List<ioT_metamodel_Attribute> getIot_metamodel_attributes() {
        return iot_metamodel_attributes;
    }

    public void addIot_metamodel_attribute(Iot_metamodel_attribute iot_metamodel_attribute) {
        this.iot_metamodel_attributes.add(iot_metamodel_attribute);
    }
    public ioT_metamodel_VirtualThing getIot_metamodel_virtualthing() {
        return iot_metamodel_virtualthing;
    }

    public void setIot_metamodel_virtualthing(ioT_metamodel_VirtualThing iot_metamodel_virtualthing) {
        this.iot_metamodel_virtualthing = iot_metamodel_virtualthing;
    }

}