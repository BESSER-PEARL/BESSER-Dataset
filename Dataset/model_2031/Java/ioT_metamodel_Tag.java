





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Tag extends Device {

    private String Name;





    private List<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings;


    public ioT_metamodel_Tag(
        String Name    ) {
        super(
        );
        this.Name = Name;
        this.iot_metamodel_physicalthings = new ArrayList<>();
    }

    public ioT_metamodel_Tag(
        String Name        ArrayList<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings    ) {
        this.Name = Name;
        this.iot_metamodel_physicalthings = iot_metamodel_physicalthings;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<ioT_metamodel_PhysicalThing> getIot_metamodel_physicalthings() {
        return iot_metamodel_physicalthings;
    }

    public void addIot_metamodel_physicalthing(Iot_metamodel_physicalthing iot_metamodel_physicalthing) {
        this.iot_metamodel_physicalthings.add(iot_metamodel_physicalthing);
    }

}