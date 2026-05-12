





import java.util.List;
import java.util.ArrayList;

public class Parking_Structure  {

    private None Type;
    private String Address;
    private String City;



    public Parking_Structure(
        None Type,        String Address,        String City    ) {
        this.Type = Type;
        this.Address = Address;
        this.City = City;
    }


    public None getType() {
        return Type;
    }

    public void setType(None Type) {
        this.Type = Type;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }


}