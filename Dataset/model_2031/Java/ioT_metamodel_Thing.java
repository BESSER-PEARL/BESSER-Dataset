





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Thing extends Entity {

    private String name;





    private List<ioT_metamodel_Thing> iot_metamodel_things;


    public ioT_metamodel_Thing(
        String name    ) {
        super(
        );
        this.name = name;
        this.iot_metamodel_things = new ArrayList<>();
    }

    public ioT_metamodel_Thing(
        String name        ArrayList<ioT_metamodel_Thing> iot_metamodel_things    ) {
        this.name = name;
        this.iot_metamodel_things = iot_metamodel_things;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ioT_metamodel_Thing> getIot_metamodel_things() {
        return iot_metamodel_things;
    }

    public void addIot_metamodel_thing(Iot_metamodel_thing iot_metamodel_thing) {
        this.iot_metamodel_things.add(iot_metamodel_thing);
    }

}