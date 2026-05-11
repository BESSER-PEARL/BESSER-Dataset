





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_VirtualThing extends Passive_Digital_Artifact, Active_Digital_Artifact {

    private String URI;





    private ioT_metamodel_Thing iot_metamodel_thing;


    public ioT_metamodel_VirtualThing(
        String URI    ) {
        super(
        );
        this.URI = URI;
    }


    public String getUri() {
        return URI;
    }

    public void setUri(String URI) {
        this.URI = URI;
    }

    public ioT_metamodel_Thing getIot_metamodel_thing() {
        return iot_metamodel_thing;
    }

    public void setIot_metamodel_thing(ioT_metamodel_Thing iot_metamodel_thing) {
        this.iot_metamodel_thing = iot_metamodel_thing;
    }

}