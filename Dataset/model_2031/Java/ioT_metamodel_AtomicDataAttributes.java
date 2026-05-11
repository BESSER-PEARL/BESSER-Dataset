





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_AtomicDataAttributes  {

    private String DeviceID;
    private String DataEncoding;





    private ioT_metamodel_AtomicData iot_metamodel_atomicdata;


    public ioT_metamodel_AtomicDataAttributes(
        String DeviceID,        String DataEncoding    ) {
        this.DeviceID = DeviceID;
        this.DataEncoding = DataEncoding;
    }


    public String getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(String DeviceID) {
        this.DeviceID = DeviceID;
    }
    public String getDataencoding() {
        return DataEncoding;
    }

    public void setDataencoding(String DataEncoding) {
        this.DataEncoding = DataEncoding;
    }

    public ioT_metamodel_AtomicData getIot_metamodel_atomicdata() {
        return iot_metamodel_atomicdata;
    }

    public void setIot_metamodel_atomicdata(ioT_metamodel_AtomicData iot_metamodel_atomicdata) {
        this.iot_metamodel_atomicdata = iot_metamodel_atomicdata;
    }

}