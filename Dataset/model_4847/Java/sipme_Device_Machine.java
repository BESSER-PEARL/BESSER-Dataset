





import java.util.List;
import java.util.ArrayList;

public class sipme_Device_Machine extends EnterpriseResource {

    private String machineMaintainer;
    private String manufacturer;



    public sipme_Device_Machine(
        String machineMaintainer,        String manufacturer    ) {
        super(
        );
        this.machineMaintainer = machineMaintainer;
        this.manufacturer = manufacturer;
    }


    public String getMachinemaintainer() {
        return machineMaintainer;
    }

    public void setMachinemaintainer(String machineMaintainer) {
        this.machineMaintainer = machineMaintainer;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }


}