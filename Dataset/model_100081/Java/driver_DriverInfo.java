





import java.util.List;
import java.util.ArrayList;

public class driver_DriverInfo  {






    private List<driver_Info> driver_infos;




    private driver_Driver driver_driver;


    public driver_DriverInfo(
    ) {
        this.driver_infos = new ArrayList<>();
    }

    public driver_DriverInfo(
        ArrayList<driver_Info> driver_infos    ) {
        this.driver_infos = driver_infos;
    }


    public List<driver_Info> getDriver_infos() {
        return driver_infos;
    }

    public void addDriver_info(Driver_info driver_info) {
        this.driver_infos.add(driver_info);
    }
    public driver_Driver getDriver_driver() {
        return driver_driver;
    }

    public void setDriver_driver(driver_Driver driver_driver) {
        this.driver_driver = driver_driver;
    }

}