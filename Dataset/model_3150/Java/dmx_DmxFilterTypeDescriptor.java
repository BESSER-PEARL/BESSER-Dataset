





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxFilterTypeDescriptor  {

    private boolean multiTyped;
    private boolean collection;
    private String single;





    private dmx_DmxFilterParameter dmx_dmxfilterparameter;




    private dmx_DmxFilter dmx_dmxfilter;




    private dmx_DmxBaseTypeSet dmx_dmxbasetypeset;


    public dmx_DmxFilterTypeDescriptor(
        boolean multiTyped,        boolean collection,        String single    ) {
        this.multiTyped = multiTyped;
        this.collection = collection;
        this.single = single;
    }


    public boolean getMultityped() {
        return multiTyped;
    }

    public void setMultityped(boolean multiTyped) {
        this.multiTyped = multiTyped;
    }
    public boolean getCollection() {
        return collection;
    }

    public void setCollection(boolean collection) {
        this.collection = collection;
    }
    public String getSingle() {
        return single;
    }

    public void setSingle(String single) {
        this.single = single;
    }

    public dmx_DmxFilterParameter getDmx_dmxfilterparameter() {
        return dmx_dmxfilterparameter;
    }

    public void setDmx_dmxfilterparameter(dmx_DmxFilterParameter dmx_dmxfilterparameter) {
        this.dmx_dmxfilterparameter = dmx_dmxfilterparameter;
    }
    public dmx_DmxFilter getDmx_dmxfilter() {
        return dmx_dmxfilter;
    }

    public void setDmx_dmxfilter(dmx_DmxFilter dmx_dmxfilter) {
        this.dmx_dmxfilter = dmx_dmxfilter;
    }
    public dmx_DmxBaseTypeSet getDmx_dmxbasetypeset() {
        return dmx_dmxbasetypeset;
    }

    public void setDmx_dmxbasetypeset(dmx_DmxBaseTypeSet dmx_dmxbasetypeset) {
        this.dmx_dmxbasetypeset = dmx_dmxbasetypeset;
    }

}