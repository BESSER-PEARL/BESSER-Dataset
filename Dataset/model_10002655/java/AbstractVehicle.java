





import java.util.List;
import java.util.ArrayList;

public class AbstractVehicle  {

    private None restrictions;
    private String type;
    private String licensePlate;



    public AbstractVehicle(
        None restrictions,        String type,        String licensePlate    ) {
        this.restrictions = restrictions;
        this.type = type;
        this.licensePlate = licensePlate;
    }


    public None getRestrictions() {
        return restrictions;
    }

    public void setRestrictions(None restrictions) {
        this.restrictions = restrictions;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getLicenseplate() {
        return licensePlate;
    }

    public void setLicenseplate(String licensePlate) {
        this.licensePlate = licensePlate;
    }


}