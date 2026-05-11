





import java.util.List;
import java.util.ArrayList;

public class ioT_Device  {

    private String name;





    private ioT_EObject iot_eobject;




    private ioT_FetchData iot_fetchdata;




    private ioT_DeviceType iot_devicetype;


    public ioT_Device(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_EObject getIot_eobject() {
        return iot_eobject;
    }

    public void setIot_eobject(ioT_EObject iot_eobject) {
        this.iot_eobject = iot_eobject;
    }
    public ioT_FetchData getIot_fetchdata() {
        return iot_fetchdata;
    }

    public void setIot_fetchdata(ioT_FetchData iot_fetchdata) {
        this.iot_fetchdata = iot_fetchdata;
    }
    public ioT_DeviceType getIot_devicetype() {
        return iot_devicetype;
    }

    public void setIot_devicetype(ioT_DeviceType iot_devicetype) {
        this.iot_devicetype = iot_devicetype;
    }

}