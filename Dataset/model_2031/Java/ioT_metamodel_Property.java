





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Property  {

    private boolean changeable;





    private ioT_metamodel_Thing iot_metamodel_thing;


    public ioT_metamodel_Property(
        boolean changeable    ) {
        this.changeable = changeable;
    }


    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }

    public ioT_metamodel_Thing getIot_metamodel_thing() {
        return iot_metamodel_thing;
    }

    public void setIot_metamodel_thing(ioT_metamodel_Thing iot_metamodel_thing) {
        this.iot_metamodel_thing = iot_metamodel_thing;
    }

}