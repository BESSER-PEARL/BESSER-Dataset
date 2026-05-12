





import java.util.List;
import java.util.ArrayList;

public class Parking_Structure  {

    private String Address;
    private None Type;
    private String City;



    public Parking_Structure(
        String Address,        None Type,        String City    ) {
        this.Address = Address;
        this.Type = Type;
        this.City = City;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public None getType() {
        return Type;
    }

    public void setType(None Type) {
        this.Type = Type;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }


}