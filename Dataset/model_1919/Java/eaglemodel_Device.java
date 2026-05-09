





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Device  {

    private String package;
    private String name;





    private eaglemodel_Devices eaglemodel_devices;


    public eaglemodel_Device(
        String package,        String name    ) {
        this.package = package;
        this.name = name;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eaglemodel_Devices getEaglemodel_devices() {
        return eaglemodel_devices;
    }

    public void setEaglemodel_devices(eaglemodel_Devices eaglemodel_devices) {
        this.eaglemodel_devices = eaglemodel_devices;
    }

}