





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxFilterParameter  {

    private String name;





    private dmx_DmxFilter dmx_dmxfilter;


    public dmx_DmxFilterParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dmx_DmxFilter getDmx_dmxfilter() {
        return dmx_dmxfilter;
    }

    public void setDmx_dmxfilter(dmx_DmxFilter dmx_dmxfilter) {
        this.dmx_dmxfilter = dmx_dmxfilter;
    }

}