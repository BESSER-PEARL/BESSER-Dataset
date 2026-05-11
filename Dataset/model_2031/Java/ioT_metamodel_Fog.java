





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Fog  {






    private ioT_metamodel_Thing iot_metamodel_thing;




    private List<ioT_metamodel_Thing> iot_metamodel_things;


    public ioT_metamodel_Fog(
    ) {
        this.iot_metamodel_things = new ArrayList<>();
    }

    public ioT_metamodel_Fog(
        ArrayList<ioT_metamodel_Thing> iot_metamodel_things    ) {
        this.iot_metamodel_things = iot_metamodel_things;
    }


    public ioT_metamodel_Thing getIot_metamodel_thing() {
        return iot_metamodel_thing;
    }

    public void setIot_metamodel_thing(ioT_metamodel_Thing iot_metamodel_thing) {
        this.iot_metamodel_thing = iot_metamodel_thing;
    }
    public List<ioT_metamodel_Thing> getIot_metamodel_things() {
        return iot_metamodel_things;
    }

    public void addIot_metamodel_thing(Iot_metamodel_thing iot_metamodel_thing) {
        this.iot_metamodel_things.add(iot_metamodel_thing);
    }

}