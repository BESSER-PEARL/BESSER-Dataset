





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxTest extends INavigableMemberContainer {

    private String name;





    private dmx_DmxModel dmx_dmxmodel;


    public dmx_DmxTest(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dmx_DmxModel getDmx_dmxmodel() {
        return dmx_dmxmodel;
    }

    public void setDmx_dmxmodel(dmx_DmxModel dmx_dmxmodel) {
        this.dmx_dmxmodel = dmx_dmxmodel;
    }

}